bl_info = {
    "name": "Mesh Particle Blend",
    "author": "J. M Areeb Uzair",
    "location": "View3D > Object",
    "category": "Object",
    "version": (1, 0, 0),
    "description": "Creates a point cloud that blends between two meshes using Geometry Nodes",
}

from mathutils import Vector
from bpy.types import Operator
from .mpb_geometry_nodes import mesh_particle_blend_node_group
from .mpb_create_mesh import create_mesh_with_n_vertices
from .mpb_shader_group import mpb_attributes_node_group
import bpy


def create_blend(self, context, apply_transform=False):
    """Takes two meshes and creates a new mesh with a Geometry Nodes group to blend particles between the two shapes"""
    # Get selected mesh objects
    selected_meshes = [
        obj for obj in bpy.context.selected_objects if obj.type == 'MESH'
    ]

    if len(selected_meshes) == 2:

        # Get the active object
        active_obj = bpy.context.active_object
        if active_obj and selected_meshes[0] != active_obj:
            selected_meshes.reverse()

        vertex_set = []

        for obj in selected_meshes:
            print(f"Object: {obj.name}")
            # Go into object mode to access the mesh data
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='OBJECT')
            # Loop through each vertex in the mesh
            vertices = []
            for vertex in obj.data.vertices:
                if apply_transform:
                    # Apply the object's world matrix to the vertex location
                    world_coord = obj.matrix_world @ vertex.co
                else:
                    world_coord = vertex.co
                # print(world_coord)
                vertices.append(world_coord)
            vertex_set.append(vertices)

            # Hide in the viewport
            obj.hide_set(True)

            # Hide in render
            obj.hide_render = True

        obj = create_mesh_with_n_vertices(vertex_set)
        geo_modifier = obj.modifiers.new(
            name="GeometryNodesModifier", type='NODES')
        # Assign the existing Geometry Nodes group to the modifier
        geo_modifier.node_group = mesh_particle_blend_node_group()
        print(f"Geometry Nodes group '{geo_modifier.node_group.name}' attached to {obj.name}.")
        mpb_attributes_node_group()
    else:
        raise Exception("Please select exactly two mesh objects.")


class OBJECT_OT_mesh_particle_blend(Operator):
    bl_idname = "mesh.create_particle_blend"
    bl_label = "Create Mesh Particle Blend"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        create_blend(self, context)
        return {'FINISHED'}

class OBJECT_OT_mesh_particle_blend_apply_transforms(Operator):
    bl_idname = "mesh.create_particle_blend_apply_transforms"
    bl_label = "Create Mesh Particle Blend Applying Transforms"
    bl_options = {'REGISTER', 'UNDO'}
    def execute(self, context):
        create_blend(self, context, True)
        return {'FINISHED'}

# Registration


def create_blend_button(self, context):
    self.layout.operator(
        OBJECT_OT_mesh_particle_blend.bl_idname,
        text="Mesh Particle Blend",
        icon='MOD_PARTICLES'
    )
    self.layout.operator(
        OBJECT_OT_mesh_particle_blend_apply_transforms.bl_idname,
        text="Mesh Particle Blend (Keep Transforms)",
        icon='MOD_PARTICLES'
    )


def register():
    bpy.utils.register_class(OBJECT_OT_mesh_particle_blend)
    bpy.utils.register_class(OBJECT_OT_mesh_particle_blend_apply_transforms)
    bpy.types.VIEW3D_MT_object.append(create_blend_button)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_mesh_particle_blend)
    bpy.utils.unregister_class(OBJECT_OT_mesh_particle_blend_apply_transforms)
    bpy.types.VIEW3D_MT_object.remove(create_blend_button)


if __name__ == "__main__":
    register()
