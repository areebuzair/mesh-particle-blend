import bpy, math, random

def create_mesh_with_n_vertices(vertex_set):
    
    n = max( len(vertex_set[0]), len(vertex_set[1]) ) 
    
    # Generate vertex coordinates in a circular pattern
    vertices = [(0, 0, 0) for i in range(n)]

    
    # Create a new mesh and object
    mesh = bpy.data.meshes.new(name="BlendedMesh")
    obj = bpy.data.objects.new(name="BlendedObject", object_data=mesh)
    
    # Link the object to the current scene
    bpy.context.collection.objects.link(obj)
    
    # Create the mesh with vertices, edges, and no faces
    mesh.from_pydata(vertices, [], [])
    mesh.update()

    # Deselect all objects
    bpy.ops.object.select_all(action='DESELECT')

    # Set the object to be active and selectable
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)

    # Add custom attribute 'pos_1' with Vector(0, 0, 0) to each vertex
    if "pos_1" not in mesh.attributes:
        pos_1_attr = mesh.attributes.new(name="pos_1", type='FLOAT_VECTOR', domain='POINT')
        for i in range(len(vertex_set[0])):
            pos_1_attr.data[i].vector = vertex_set[0][i]
            
    if "pos_2" not in mesh.attributes:
        pos_2_attr = mesh.attributes.new(name="pos_2", type='FLOAT_VECTOR', domain='POINT')
        for i in range(len(vertex_set[1])):
            pos_2_attr.data[i].vector = vertex_set[1][i]
    
    if len(vertex_set[1]) < len(vertex_set[0]):      
        for i in range(len(vertex_set[1]), len(mesh.vertices)):
            pos_2_attr.data[i].vector = random.choice(vertex_set[1])
            
    else:      
        for i in range(len(vertex_set[0]), len(mesh.vertices)):
            pos_1_attr.data[i].vector = random.choice(vertex_set[0])

    print(f"Created object '{obj.name}' with {n} vertices.")
    
    return obj