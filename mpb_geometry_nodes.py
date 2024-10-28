import bpy, mathutils

#initialize mesh_particle_blend node group
def mesh_particle_blend_node_group():
	mesh_particle_blend = bpy.data.node_groups.new(type = 'GeometryNodeTree', name = "Mesh Particle Blend")

	mesh_particle_blend.is_modifier = True
	
	#mesh_particle_blend interface
	#Socket Geometry
	geometry_socket = mesh_particle_blend.interface.new_socket(name = "Geometry", in_out='OUTPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket.attribute_domain = 'POINT'
	
	#Socket Geometry
	geometry_socket_1 = mesh_particle_blend.interface.new_socket(name = "Geometry", in_out='INPUT', socket_type = 'NodeSocketGeometry')
	geometry_socket_1.attribute_domain = 'POINT'
	
	#Socket Factor
	factor_socket = mesh_particle_blend.interface.new_socket(name = "Factor", in_out='INPUT', socket_type = 'NodeSocketFloat')
	factor_socket.default_value = 0.0
	factor_socket.min_value = 0.0
	factor_socket.max_value = 1.0
	factor_socket.subtype = 'FACTOR'
	factor_socket.attribute_domain = 'POINT'
	factor_socket.description = "The blend factor between two shapes"
	
	#Socket Seed
	seed_socket = mesh_particle_blend.interface.new_socket(name = "Seed", in_out='INPUT', socket_type = 'NodeSocketFloat')
	seed_socket.default_value = 0.0
	seed_socket.min_value = -1000.0
	seed_socket.max_value = 1000.0
	seed_socket.subtype = 'NONE'
	seed_socket.attribute_domain = 'POINT'
	seed_socket.description = "The seed for the noise. Is animatable"
	
	#Socket Turbulence
	turbulence_socket = mesh_particle_blend.interface.new_socket(name = "Turbulence", in_out='INPUT', socket_type = 'NodeSocketFloat')
	turbulence_socket.default_value = 1.0
	turbulence_socket.min_value = -1000.0
	turbulence_socket.max_value = 1000.0
	turbulence_socket.subtype = 'NONE'
	turbulence_socket.attribute_domain = 'POINT'
	turbulence_socket.description = "How turbulent the noise is"
	
	#Socket Strength
	strength_socket = mesh_particle_blend.interface.new_socket(name = "Strength", in_out='INPUT', socket_type = 'NodeSocketFloat')
	strength_socket.default_value = 10.0
	strength_socket.min_value = -10000.0
	strength_socket.max_value = 10000.0
	strength_socket.subtype = 'NONE'
	strength_socket.attribute_domain = 'POINT'
	strength_socket.description = "How far the turbulence will spread. At 0, a linear blend will occur"
	
	#Socket Spread Direction
	spread_direction_socket = mesh_particle_blend.interface.new_socket(name = "Spread Direction", in_out='INPUT', socket_type = 'NodeSocketVector')
	spread_direction_socket.default_value = (1.0, 1.0, 1.0)
	spread_direction_socket.min_value = 0.0
	spread_direction_socket.max_value = 1.0
	spread_direction_socket.subtype = 'NONE'
	spread_direction_socket.attribute_domain = 'POINT'
	spread_direction_socket.description = "The directions in which the particles will spread"
	
	#Socket Use Object
	use_object_socket = mesh_particle_blend.interface.new_socket(name = "Use Object", in_out='INPUT', socket_type = 'NodeSocketBool')
	use_object_socket.default_value = False
	use_object_socket.attribute_domain = 'POINT'
	use_object_socket.description = "Use Objects as Particles"
	
	#Socket Object
	object_socket = mesh_particle_blend.interface.new_socket(name = "Object", in_out='INPUT', socket_type = 'NodeSocketObject')
	object_socket.attribute_domain = 'POINT'
	object_socket.description = "The instance object for the particles"
	
	#Socket Randomize Rotation
	randomize_rotation_socket = mesh_particle_blend.interface.new_socket(name = "Randomize Rotation", in_out='INPUT', socket_type = 'NodeSocketFloat')
	randomize_rotation_socket.default_value = 0.0
	randomize_rotation_socket.min_value = 0.0
	randomize_rotation_socket.max_value = 1.0
	randomize_rotation_socket.subtype = 'FACTOR'
	randomize_rotation_socket.attribute_domain = 'POINT'
	
	#Socket Randomize Scale
	randomize_scale_socket = mesh_particle_blend.interface.new_socket(name = "Randomize Scale", in_out='INPUT', socket_type = 'NodeSocketFloat')
	randomize_scale_socket.default_value = 0.0
	randomize_scale_socket.min_value = 0.0
	randomize_scale_socket.max_value = 1.0
	randomize_scale_socket.subtype = 'FACTOR'
	randomize_scale_socket.attribute_domain = 'POINT'
	
	
	#initialize mesh_particle_blend nodes
	#node Group Input
	group_input = mesh_particle_blend.nodes.new("NodeGroupInput")
	group_input.name = "Group Input"
	
	#node Group Output
	group_output = mesh_particle_blend.nodes.new("NodeGroupOutput")
	group_output.name = "Group Output"
	group_output.is_active_output = True
	
	#node Instance on Points
	instance_on_points = mesh_particle_blend.nodes.new("GeometryNodeInstanceOnPoints")
	instance_on_points.name = "Instance on Points"
	#Selection
	instance_on_points.inputs[1].default_value = True
	#Pick Instance
	instance_on_points.inputs[3].default_value = False
	#Instance Index
	instance_on_points.inputs[4].default_value = 0
	
	#node Set Position
	set_position = mesh_particle_blend.nodes.new("GeometryNodeSetPosition")
	set_position.name = "Set Position"
	#Selection
	set_position.inputs[1].default_value = True
	
	#node Named Attribute
	named_attribute = mesh_particle_blend.nodes.new("GeometryNodeInputNamedAttribute")
	named_attribute.name = "Named Attribute"
	named_attribute.data_type = 'FLOAT_VECTOR'
	#Name
	named_attribute.inputs[0].default_value = "pos_1"
	
	#node Named Attribute.001
	named_attribute_001 = mesh_particle_blend.nodes.new("GeometryNodeInputNamedAttribute")
	named_attribute_001.name = "Named Attribute.001"
	named_attribute_001.data_type = 'FLOAT_VECTOR'
	#Name
	named_attribute_001.inputs[0].default_value = "pos_2"
	
	#node Mix
	mix = mesh_particle_blend.nodes.new("ShaderNodeMix")
	mix.name = "Mix"
	mix.blend_type = 'MIX'
	mix.clamp_factor = True
	mix.clamp_result = False
	mix.data_type = 'VECTOR'
	mix.factor_mode = 'UNIFORM'
	
	#node Mix.001
	mix_001 = mesh_particle_blend.nodes.new("ShaderNodeMix")
	mix_001.name = "Mix.001"
	mix_001.blend_type = 'MIX'
	mix_001.clamp_factor = True
	mix_001.clamp_result = False
	mix_001.data_type = 'VECTOR'
	mix_001.factor_mode = 'UNIFORM'
	#A_Vector
	mix_001.inputs[4].default_value = (0.0, 0.0, 0.0)
	
	#node Math
	math = mesh_particle_blend.nodes.new("ShaderNodeMath")
	math.name = "Math"
	math.operation = 'SUBTRACT'
	math.use_clamp = False
	#Value_001
	math.inputs[1].default_value = 0.5
	
	#node Math.001
	math_001 = mesh_particle_blend.nodes.new("ShaderNodeMath")
	math_001.name = "Math.001"
	math_001.operation = 'ABSOLUTE'
	math_001.use_clamp = False
	
	#node Math.002
	math_002 = mesh_particle_blend.nodes.new("ShaderNodeMath")
	math_002.name = "Math.002"
	math_002.operation = 'MULTIPLY'
	math_002.use_clamp = False
	#Value_001
	math_002.inputs[1].default_value = 2.0
	
	#node Math.003
	math_003 = mesh_particle_blend.nodes.new("ShaderNodeMath")
	math_003.name = "Math.003"
	math_003.operation = 'SUBTRACT'
	math_003.use_clamp = False
	#Value
	math_003.inputs[0].default_value = 1.0
	
	#node Group Input.001
	group_input_001 = mesh_particle_blend.nodes.new("NodeGroupInput")
	group_input_001.name = "Group Input.001"
	
	#node Vector Math
	vector_math = mesh_particle_blend.nodes.new("ShaderNodeVectorMath")
	vector_math.name = "Vector Math"
	vector_math.operation = 'SUBTRACT'
	#Vector_001
	vector_math.inputs[1].default_value = (0.5, 0.5, 0.5)
	
	#node Vector Math.001
	vector_math_001 = mesh_particle_blend.nodes.new("ShaderNodeVectorMath")
	vector_math_001.name = "Vector Math.001"
	vector_math_001.operation = 'SCALE'
	
	#node Noise Texture
	noise_texture = mesh_particle_blend.nodes.new("ShaderNodeTexNoise")
	noise_texture.name = "Noise Texture"
	noise_texture.noise_dimensions = '4D'
	noise_texture.noise_type = 'FBM'
	noise_texture.normalize = True
	#Detail
	noise_texture.inputs[3].default_value = 2.0
	#Roughness
	noise_texture.inputs[4].default_value = 0.5
	#Lacunarity
	noise_texture.inputs[5].default_value = 2.0
	#Distortion
	noise_texture.inputs[8].default_value = 0.0
	
	#node Reroute
	reroute = mesh_particle_blend.nodes.new("NodeReroute")
	reroute.name = "Reroute"
	#node Object Info
	object_info = mesh_particle_blend.nodes.new("GeometryNodeObjectInfo")
	object_info.name = "Object Info"
	object_info.transform_space = 'ORIGINAL'
	#As Instance
	object_info.inputs[1].default_value = True
	
	#node Group Input.002
	group_input_002 = mesh_particle_blend.nodes.new("NodeGroupInput")
	group_input_002.name = "Group Input.002"
	
	#node Vector Math.002
	vector_math_002 = mesh_particle_blend.nodes.new("ShaderNodeVectorMath")
	vector_math_002.name = "Vector Math.002"
	vector_math_002.operation = 'ADD'
	
	#node Switch
	switch = mesh_particle_blend.nodes.new("GeometryNodeSwitch")
	switch.name = "Switch"
	switch.input_type = 'GEOMETRY'
	
	#node Mesh to Points
	mesh_to_points = mesh_particle_blend.nodes.new("GeometryNodeMeshToPoints")
	mesh_to_points.name = "Mesh to Points"
	mesh_to_points.mode = 'VERTICES'
	#Selection
	mesh_to_points.inputs[1].default_value = True
	#Position
	mesh_to_points.inputs[2].default_value = (0.0, 0.0, 0.0)
	#Radius
	mesh_to_points.inputs[3].default_value = 0.020000001415610313
	
	#node Group Input.003
	group_input_003 = mesh_particle_blend.nodes.new("NodeGroupInput")
	group_input_003.name = "Group Input.003"
	
	#node Mix.002
	mix_002 = mesh_particle_blend.nodes.new("ShaderNodeMix")
	mix_002.name = "Mix.002"
	mix_002.blend_type = 'MIX'
	mix_002.clamp_factor = True
	mix_002.clamp_result = False
	mix_002.data_type = 'VECTOR'
	mix_002.factor_mode = 'NON_UNIFORM'
	#A_Vector
	mix_002.inputs[4].default_value = (0.0, 0.0, 0.0)
	
	#node Group Input.004
	group_input_004 = mesh_particle_blend.nodes.new("NodeGroupInput")
	group_input_004.name = "Group Input.004"
	
	#node Float Curve
	float_curve = mesh_particle_blend.nodes.new("ShaderNodeFloatCurve")
	float_curve.name = "Float Curve"
	#mapping settings
	float_curve.mapping.extend = 'EXTRAPOLATED'
	float_curve.mapping.tone = 'STANDARD'
	float_curve.mapping.black_level = (0.0, 0.0, 0.0)
	float_curve.mapping.white_level = (1.0, 1.0, 1.0)
	float_curve.mapping.clip_min_x = 0.0
	float_curve.mapping.clip_min_y = 0.0
	float_curve.mapping.clip_max_x = 1.0
	float_curve.mapping.clip_max_y = 1.0
	float_curve.mapping.use_clip = True
	#curve 0
	float_curve_curve_0 = float_curve.mapping.curves[0]
	float_curve_curve_0_point_0 = float_curve_curve_0.points[0]
	float_curve_curve_0_point_0.location = (0.0, 0.0)
	float_curve_curve_0_point_0.handle_type = 'AUTO'
	float_curve_curve_0_point_1 = float_curve_curve_0.points[1]
	float_curve_curve_0_point_1.location = (0.8731117248535156, 0.9827585220336914)
	float_curve_curve_0_point_1.handle_type = 'AUTO'
	float_curve_curve_0_point_2 = float_curve_curve_0.points.new(1.0, 1.0)
	float_curve_curve_0_point_2.handle_type = 'AUTO'
	#update curve after changes
	float_curve.mapping.update()
	#Factor
	float_curve.inputs[0].default_value = 1.0
	
	#node Store Named Attribute
	store_named_attribute = mesh_particle_blend.nodes.new("GeometryNodeStoreNamedAttribute")
	store_named_attribute.name = "Store Named Attribute"
	store_named_attribute.data_type = 'INT'
	store_named_attribute.domain = 'INSTANCE'
	#Selection
	store_named_attribute.inputs[1].default_value = True
	#Name
	store_named_attribute.inputs[2].default_value = "Index"
	
	#node Index
	index = mesh_particle_blend.nodes.new("GeometryNodeInputIndex")
	index.name = "Index"
	
	#node Store Named Attribute.001
	store_named_attribute_001 = mesh_particle_blend.nodes.new("GeometryNodeStoreNamedAttribute")
	store_named_attribute_001.name = "Store Named Attribute.001"
	store_named_attribute_001.data_type = 'FLOAT_VECTOR'
	store_named_attribute_001.domain = 'INSTANCE'
	#Selection
	store_named_attribute_001.inputs[1].default_value = True
	#Name
	store_named_attribute_001.inputs[2].default_value = "Position"
	
	#node Position
	position = mesh_particle_blend.nodes.new("GeometryNodeInputPosition")
	position.name = "Position"
	
	#node Vector Math.003
	vector_math_003 = mesh_particle_blend.nodes.new("ShaderNodeVectorMath")
	vector_math_003.name = "Vector Math.003"
	vector_math_003.operation = 'ADD'
	
	#node Random Value
	random_value = mesh_particle_blend.nodes.new("FunctionNodeRandomValue")
	random_value.name = "Random Value"
	random_value.data_type = 'FLOAT_VECTOR'
	#Min
	random_value.inputs[0].default_value = (0.0, 0.0, 0.0)
	#Max
	random_value.inputs[1].default_value = (6.2831854820251465, 6.2831854820251465, 6.2831854820251465)
	#ID
	random_value.inputs[7].default_value = 0
	#Seed
	random_value.inputs[8].default_value = 0
	
	#node Vector Math.004
	vector_math_004 = mesh_particle_blend.nodes.new("ShaderNodeVectorMath")
	vector_math_004.name = "Vector Math.004"
	vector_math_004.operation = 'SCALE'
	
	#node Group Input.005
	group_input_005 = mesh_particle_blend.nodes.new("NodeGroupInput")
	group_input_005.name = "Group Input.005"
	
	#node Vector Math.005
	vector_math_005 = mesh_particle_blend.nodes.new("ShaderNodeVectorMath")
	vector_math_005.name = "Vector Math.005"
	vector_math_005.operation = 'SCALE'
	
	#node Random Value.001
	random_value_001 = mesh_particle_blend.nodes.new("FunctionNodeRandomValue")
	random_value_001.name = "Random Value.001"
	random_value_001.data_type = 'FLOAT'
	#Min_001
	random_value_001.inputs[2].default_value = 0.0
	#Max_001
	random_value_001.inputs[3].default_value = 1.0
	#ID
	random_value_001.inputs[7].default_value = 0
	#Seed
	random_value_001.inputs[8].default_value = 0
	
	#node Mix.003
	mix_003 = mesh_particle_blend.nodes.new("ShaderNodeMix")
	mix_003.name = "Mix.003"
	mix_003.blend_type = 'MIX'
	mix_003.clamp_factor = True
	mix_003.clamp_result = False
	mix_003.data_type = 'VECTOR'
	mix_003.factor_mode = 'UNIFORM'
	
	#node Group Input.006
	group_input_006 = mesh_particle_blend.nodes.new("NodeGroupInput")
	group_input_006.name = "Group Input.006"
	
	#node Store Named Attribute.002
	store_named_attribute_002 = mesh_particle_blend.nodes.new("GeometryNodeStoreNamedAttribute")
	store_named_attribute_002.name = "Store Named Attribute.002"
	store_named_attribute_002.data_type = 'FLOAT'
	store_named_attribute_002.domain = 'POINT'
	#Selection
	store_named_attribute_002.inputs[1].default_value = True
	#Name
	store_named_attribute_002.inputs[2].default_value = "Factor"
	
	
	
	
	#Set locations
	group_input.location = (-1205.496337890625, 142.00987243652344)
	group_output.location = (2586.229736328125, -56.09250259399414)
	instance_on_points.location = (1678.9481201171875, -116.01433563232422)
	set_position.location = (696.4578247070312, 154.6160125732422)
	named_attribute.location = (-1067.5220947265625, -171.9987030029297)
	named_attribute_001.location = (-1062.5640869140625, -363.4000244140625)
	mix.location = (-783.1732788085938, -171.3526153564453)
	mix_001.location = (176.22796630859375, -63.4924201965332)
	math.location = (-835.4188842773438, 6.803090572357178)
	math_001.location = (-672.7169189453125, -4.46380615234375)
	math_002.location = (-510.0502014160156, 2.779200315475464)
	math_003.location = (-328.15386962890625, 0.7134348750114441)
	group_input_001.location = (-783.0807495117188, -558.9899291992188)
	vector_math.location = (-355.0063781738281, -310.9267578125)
	vector_math_001.location = (-166.67933654785156, -333.161865234375)
	noise_texture.location = (-535.6362915039062, -326.6654052734375)
	reroute.location = (-288.91485595703125, -661.64306640625)
	object_info.location = (811.484619140625, -319.4120178222656)
	group_input_002.location = (619.0313110351562, -270.8577880859375)
	vector_math_002.location = (-788.4248657226562, -384.8642578125)
	switch.location = (2366.27734375, -13.922266960144043)
	mesh_to_points.location = (1272.4427490234375, 173.5979461669922)
	group_input_003.location = (1261.7144775390625, 455.4060974121094)
	mix_002.location = (358.6495666503906, -57.170902252197266)
	group_input_004.location = (89.48336791992188, -391.780517578125)
	float_curve.location = (-109.21344757080078, -3.0170440673828125)
	store_named_attribute.location = (1990.171142578125, -123.61772918701172)
	index.location = (1702.7413330078125, -349.8357238769531)
	store_named_attribute_001.location = (2165.73681640625, -199.6058349609375)
	position.location = (1705.35498046875, -457.1595458984375)
	vector_math_003.location = (1177.845947265625, -573.2647094726562)
	random_value.location = (747.0966186523438, -556.8772583007812)
	vector_math_004.location = (987.8305053710938, -690.4440307617188)
	group_input_005.location = (743.0045776367188, -850.104248046875)
	vector_math_005.location = (1183.0975341796875, -391.6228332519531)
	random_value_001.location = (815.7630004882812, -147.4152374267578)
	mix_003.location = (1380.5552978515625, -286.0567932128906)
	group_input_006.location = (1072.4093017578125, -118.2861099243164)
	store_named_attribute_002.location = (-790.6491088867188, 245.50628662109375)
	
	#Set dimensions
	group_input.width, group_input.height = 140.0, 100.0
	group_output.width, group_output.height = 140.0, 100.0
	instance_on_points.width, instance_on_points.height = 140.0, 100.0
	set_position.width, set_position.height = 140.0, 100.0
	named_attribute.width, named_attribute.height = 140.0, 100.0
	named_attribute_001.width, named_attribute_001.height = 140.0, 100.0
	mix.width, mix.height = 140.0, 100.0
	mix_001.width, mix_001.height = 140.0, 100.0
	math.width, math.height = 140.0, 100.0
	math_001.width, math_001.height = 140.0, 100.0
	math_002.width, math_002.height = 140.0, 100.0
	math_003.width, math_003.height = 140.0, 100.0
	group_input_001.width, group_input_001.height = 140.0, 100.0
	vector_math.width, vector_math.height = 140.0, 100.0
	vector_math_001.width, vector_math_001.height = 140.0, 100.0
	noise_texture.width, noise_texture.height = 140.0, 100.0
	reroute.width, reroute.height = 16.0, 100.0
	object_info.width, object_info.height = 140.0, 100.0
	group_input_002.width, group_input_002.height = 140.0, 100.0
	vector_math_002.width, vector_math_002.height = 140.0, 100.0
	switch.width, switch.height = 140.0, 100.0
	mesh_to_points.width, mesh_to_points.height = 140.0, 100.0
	group_input_003.width, group_input_003.height = 140.0, 100.0
	mix_002.width, mix_002.height = 140.0, 100.0
	group_input_004.width, group_input_004.height = 140.0, 100.0
	float_curve.width, float_curve.height = 240.0, 100.0
	store_named_attribute.width, store_named_attribute.height = 140.0, 100.0
	index.width, index.height = 140.0, 100.0
	store_named_attribute_001.width, store_named_attribute_001.height = 140.0, 100.0
	position.width, position.height = 140.0, 100.0
	vector_math_003.width, vector_math_003.height = 140.0, 100.0
	random_value.width, random_value.height = 140.0, 100.0
	vector_math_004.width, vector_math_004.height = 140.0, 100.0
	group_input_005.width, group_input_005.height = 140.0, 100.0
	vector_math_005.width, vector_math_005.height = 140.0, 100.0
	random_value_001.width, random_value_001.height = 140.0, 100.0
	mix_003.width, mix_003.height = 140.0, 100.0
	group_input_006.width, group_input_006.height = 140.0, 100.0
	store_named_attribute_002.width, store_named_attribute_002.height = 140.0, 100.0
	
	#initialize mesh_particle_blend links
	#set_position.Geometry -> instance_on_points.Points
	mesh_particle_blend.links.new(set_position.outputs[0], instance_on_points.inputs[0])
	#store_named_attribute_002.Geometry -> set_position.Geometry
	mesh_particle_blend.links.new(store_named_attribute_002.outputs[0], set_position.inputs[0])
	#named_attribute.Attribute -> mix.A
	mesh_particle_blend.links.new(named_attribute.outputs[0], mix.inputs[4])
	#named_attribute_001.Attribute -> mix.B
	mesh_particle_blend.links.new(named_attribute_001.outputs[0], mix.inputs[5])
	#switch.Output -> group_output.Geometry
	mesh_particle_blend.links.new(switch.outputs[0], group_output.inputs[0])
	#group_input.Factor -> mix.Factor
	mesh_particle_blend.links.new(group_input.outputs[1], mix.inputs[0])
	#float_curve.Value -> mix_001.Factor
	mesh_particle_blend.links.new(float_curve.outputs[0], mix_001.inputs[0])
	#group_input.Factor -> math.Value
	mesh_particle_blend.links.new(group_input.outputs[1], math.inputs[0])
	#math.Value -> math_001.Value
	mesh_particle_blend.links.new(math.outputs[0], math_001.inputs[0])
	#math_001.Value -> math_002.Value
	mesh_particle_blend.links.new(math_001.outputs[0], math_002.inputs[0])
	#math_002.Value -> math_003.Value
	mesh_particle_blend.links.new(math_002.outputs[0], math_003.inputs[1])
	#noise_texture.Color -> vector_math.Vector
	mesh_particle_blend.links.new(noise_texture.outputs[1], vector_math.inputs[0])
	#vector_math.Vector -> vector_math_001.Vector
	mesh_particle_blend.links.new(vector_math.outputs[0], vector_math_001.inputs[0])
	#reroute.Output -> vector_math_001.Scale
	mesh_particle_blend.links.new(reroute.outputs[0], vector_math_001.inputs[3])
	#group_input_001.Turbulence -> noise_texture.Scale
	mesh_particle_blend.links.new(group_input_001.outputs[3], noise_texture.inputs[2])
	#group_input_001.Seed -> noise_texture.W
	mesh_particle_blend.links.new(group_input_001.outputs[2], noise_texture.inputs[1])
	#group_input_001.Strength -> reroute.Input
	mesh_particle_blend.links.new(group_input_001.outputs[4], reroute.inputs[0])
	#vector_math_001.Vector -> mix_001.B
	mesh_particle_blend.links.new(vector_math_001.outputs[0], mix_001.inputs[5])
	#object_info.Geometry -> instance_on_points.Instance
	mesh_particle_blend.links.new(object_info.outputs[3], instance_on_points.inputs[2])
	#group_input_002.Object -> object_info.Object
	mesh_particle_blend.links.new(group_input_002.outputs[7], object_info.inputs[0])
	#mix_003.Result -> instance_on_points.Scale
	mesh_particle_blend.links.new(mix_003.outputs[1], instance_on_points.inputs[6])
	#vector_math_003.Vector -> instance_on_points.Rotation
	mesh_particle_blend.links.new(vector_math_003.outputs[0], instance_on_points.inputs[5])
	#mix.Result -> set_position.Position
	mesh_particle_blend.links.new(mix.outputs[1], set_position.inputs[2])
	#mix_002.Result -> set_position.Offset
	mesh_particle_blend.links.new(mix_002.outputs[1], set_position.inputs[3])
	#named_attribute.Attribute -> vector_math_002.Vector
	mesh_particle_blend.links.new(named_attribute.outputs[0], vector_math_002.inputs[0])
	#named_attribute_001.Attribute -> vector_math_002.Vector
	mesh_particle_blend.links.new(named_attribute_001.outputs[0], vector_math_002.inputs[1])
	#vector_math_002.Vector -> noise_texture.Vector
	mesh_particle_blend.links.new(vector_math_002.outputs[0], noise_texture.inputs[0])
	#set_position.Geometry -> mesh_to_points.Mesh
	mesh_particle_blend.links.new(set_position.outputs[0], mesh_to_points.inputs[0])
	#group_input_003.Use Object -> switch.Switch
	mesh_particle_blend.links.new(group_input_003.outputs[6], switch.inputs[0])
	#mix_001.Result -> mix_002.B
	mesh_particle_blend.links.new(mix_001.outputs[1], mix_002.inputs[5])
	#group_input_004.Spread Direction -> mix_002.Factor
	mesh_particle_blend.links.new(group_input_004.outputs[5], mix_002.inputs[1])
	#mesh_to_points.Points -> switch.False
	mesh_particle_blend.links.new(mesh_to_points.outputs[0], switch.inputs[1])
	#store_named_attribute_001.Geometry -> switch.True
	mesh_particle_blend.links.new(store_named_attribute_001.outputs[0], switch.inputs[2])
	#math_003.Value -> float_curve.Value
	mesh_particle_blend.links.new(math_003.outputs[0], float_curve.inputs[1])
	#instance_on_points.Instances -> store_named_attribute.Geometry
	mesh_particle_blend.links.new(instance_on_points.outputs[0], store_named_attribute.inputs[0])
	#index.Index -> store_named_attribute.Value
	mesh_particle_blend.links.new(index.outputs[0], store_named_attribute.inputs[3])
	#store_named_attribute.Geometry -> store_named_attribute_001.Geometry
	mesh_particle_blend.links.new(store_named_attribute.outputs[0], store_named_attribute_001.inputs[0])
	#position.Position -> store_named_attribute_001.Value
	mesh_particle_blend.links.new(position.outputs[0], store_named_attribute_001.inputs[3])
	#object_info.Rotation -> vector_math_003.Vector
	mesh_particle_blend.links.new(object_info.outputs[1], vector_math_003.inputs[0])
	#vector_math_004.Vector -> vector_math_003.Vector
	mesh_particle_blend.links.new(vector_math_004.outputs[0], vector_math_003.inputs[1])
	#random_value.Value -> vector_math_004.Vector
	mesh_particle_blend.links.new(random_value.outputs[0], vector_math_004.inputs[0])
	#group_input_005.Randomize Rotation -> vector_math_004.Scale
	mesh_particle_blend.links.new(group_input_005.outputs[8], vector_math_004.inputs[3])
	#object_info.Scale -> vector_math_005.Vector
	mesh_particle_blend.links.new(object_info.outputs[2], vector_math_005.inputs[0])
	#random_value_001.Value -> vector_math_005.Scale
	mesh_particle_blend.links.new(random_value_001.outputs[1], vector_math_005.inputs[3])
	#vector_math_005.Vector -> mix_003.B
	mesh_particle_blend.links.new(vector_math_005.outputs[0], mix_003.inputs[5])
	#object_info.Scale -> mix_003.A
	mesh_particle_blend.links.new(object_info.outputs[2], mix_003.inputs[4])
	#group_input_006.Randomize Scale -> mix_003.Factor
	mesh_particle_blend.links.new(group_input_006.outputs[9], mix_003.inputs[0])
	#group_input.Geometry -> store_named_attribute_002.Geometry
	mesh_particle_blend.links.new(group_input.outputs[0], store_named_attribute_002.inputs[0])
	#group_input.Factor -> store_named_attribute_002.Value
	mesh_particle_blend.links.new(group_input.outputs[1], store_named_attribute_002.inputs[3])
	return mesh_particle_blend


