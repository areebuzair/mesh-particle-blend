# mesh-particle-blend
A Blender addon that creates a point cloud that blends between two meshes using Geometry Nodes

## Install
Install the latest version of the addon from [here](https://github.com/areebuzair/mesh-particle-blend/releases).

> [!WARNING]
> This version is a test version that has only been used on Blender 4.1.1. It works on 4.2.0, but the Geometry Nodes setup becomes incorrect. 

## Use Addon
![Screenshot 2024-11-03 160026](https://github.com/user-attachments/assets/fdea8880-2cfc-4a6f-aa03-301c3095569c)

Select two meshes, then in the `Object` menu choose either `Mesh Particle Blend` (objects will lose all transforms), or chooses `Mesh Particle Blend (Keep Transforms)`.

The created point cloud will have a Geometry Nodes modifier applied to it, which will be used to control the effect.

> [!important]
> In the shading tab, a new Node group called `mpb_attributes` will be available.
> If an object is chosen to render as the point cloud instance, this node group can be used to access various properties of the point cloud.

## Credits
Thanks to [NodeToPython](https://github.com/BrendanParmer/NodeToPython) for making this project possible.
