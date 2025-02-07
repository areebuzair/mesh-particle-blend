# mesh-particle-blend
A Blender addon that creates a point cloud that blends between two meshes using Geometry Nodes

## Install
Install the latest version of the addon from [here](https://github.com/areebuzair/mesh-particle-blend/releases).

> [!WARNING]
> This version works on Blender 4.2. To use it on Blender 4.1, install version 1.0.0.

## Use Addon
![Screenshot 2024-11-03 160026](https://github.com/user-attachments/assets/fdea8880-2cfc-4a6f-aa03-301c3095569c)

Select two meshes, then in the `Object` menu choose either `Mesh Particle Blend` (objects will lose all transforms), or chooses `Mesh Particle Blend (Keep Transforms)`.

The created point cloud will have a Geometry Nodes modifier applied to it, which will be used to control the effect.

> [!important]
> In the shading tab, a new Node group called `mpb_attributes` will be available.
> If an object is chosen to render as the point cloud instance, this node group can be used to access various properties of the point cloud.
> Make sure the material is applied to the object being instanced, not to the point cloud.

![Screenshot 2025-02-03 141905](https://github.com/user-attachments/assets/36eb5a3b-ea0a-4c7a-8cd1-5bfeb36864c3)

## Credits
Thanks to [NodeToPython](https://github.com/BrendanParmer/NodeToPython) for making this project possible.
