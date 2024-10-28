import bpy, mathutils

#initialize MPB_Attributes node group
def mpb_attributes_node_group():
    
    if "MPB_Attributes" in bpy.data.node_groups: return

    mpb_attributes = bpy.data.node_groups.new(type = 'ShaderNodeTree', name = "MPB_Attributes")
    
    #mpb_attributes interface
    #Socket Index
    index_socket = mpb_attributes.interface.new_socket(name = "Index", in_out='OUTPUT', socket_type = 'NodeSocketInt')
    index_socket.default_value = 0
    index_socket.min_value = -2147483648
    index_socket.max_value = 2147483647
    index_socket.subtype = 'NONE'
    index_socket.attribute_domain = 'POINT'
    
    #Socket Position
    position_socket = mpb_attributes.interface.new_socket(name = "Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    position_socket.default_value = (0.0, 0.0, 0.0)
    position_socket.min_value = -3.4028234663852886e+38
    position_socket.max_value = 3.4028234663852886e+38
    position_socket.subtype = 'NONE'
    position_socket.attribute_domain = 'POINT'
    
    #Socket Initial Position
    initial_position_socket = mpb_attributes.interface.new_socket(name = "Initial Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    initial_position_socket.default_value = (0.0, 0.0, 0.0)
    initial_position_socket.min_value = -3.4028234663852886e+38
    initial_position_socket.max_value = 3.4028234663852886e+38
    initial_position_socket.subtype = 'NONE'
    initial_position_socket.attribute_domain = 'POINT'
    
    #Socket Final Position
    final_position_socket = mpb_attributes.interface.new_socket(name = "Final Position", in_out='OUTPUT', socket_type = 'NodeSocketVector')
    final_position_socket.default_value = (0.0, 0.0, 0.0)
    final_position_socket.min_value = -3.4028234663852886e+38
    final_position_socket.max_value = 3.4028234663852886e+38
    final_position_socket.subtype = 'NONE'
    final_position_socket.attribute_domain = 'POINT'
    
    #Socket Random Per Instance
    random_per_instance_socket = mpb_attributes.interface.new_socket(name = "Random Per Instance", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    random_per_instance_socket.default_value = 0.0
    random_per_instance_socket.min_value = -3.4028234663852886e+38
    random_per_instance_socket.max_value = 3.4028234663852886e+38
    random_per_instance_socket.subtype = 'NONE'
    random_per_instance_socket.attribute_domain = 'POINT'
    
    #Socket Displacement
    displacement_socket = mpb_attributes.interface.new_socket(name = "Displacement", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    displacement_socket.default_value = 0.0
    displacement_socket.min_value = -3.4028234663852886e+38
    displacement_socket.max_value = 3.4028234663852886e+38
    displacement_socket.subtype = 'DISTANCE'
    displacement_socket.attribute_domain = 'POINT'
    
    #Socket Factor
    factor_socket = mpb_attributes.interface.new_socket(name = "Factor", in_out='OUTPUT', socket_type = 'NodeSocketFloat')
    factor_socket.default_value = 0.0
    factor_socket.min_value = -3.4028234663852886e+38
    factor_socket.max_value = 3.4028234663852886e+38
    factor_socket.subtype = 'FACTOR'
    factor_socket.attribute_domain = 'POINT'
    
    
    #initialize mpb_attributes nodes
    #node Group Output
    group_output = mpb_attributes.nodes.new("NodeGroupOutput")
    group_output.name = "Group Output"
    group_output.is_active_output = True
    
    #node Group Input
    group_input = mpb_attributes.nodes.new("NodeGroupInput")
    group_input.name = "Group Input"
    
    #node Attribute
    attribute = mpb_attributes.nodes.new("ShaderNodeAttribute")
    attribute.name = "Attribute"
    attribute.attribute_name = "Index"
    attribute.attribute_type = 'INSTANCER'
    
    #node Attribute.001
    attribute_001 = mpb_attributes.nodes.new("ShaderNodeAttribute")
    attribute_001.name = "Attribute.001"
    attribute_001.attribute_name = "Position"
    attribute_001.attribute_type = 'INSTANCER'
    
    #node Attribute.002
    attribute_002 = mpb_attributes.nodes.new("ShaderNodeAttribute")
    attribute_002.name = "Attribute.002"
    attribute_002.attribute_name = "pos_1"
    attribute_002.attribute_type = 'INSTANCER'
    
    #node Attribute.003
    attribute_003 = mpb_attributes.nodes.new("ShaderNodeAttribute")
    attribute_003.name = "Attribute.003"
    attribute_003.attribute_name = "pos_2"
    attribute_003.attribute_type = 'INSTANCER'
    
    #node Vector Math
    vector_math = mpb_attributes.nodes.new("ShaderNodeVectorMath")
    vector_math.name = "Vector Math"
    vector_math.operation = 'DISTANCE'
    
    #node Vector Math.001
    vector_math_001 = mpb_attributes.nodes.new("ShaderNodeVectorMath")
    vector_math_001.name = "Vector Math.001"
    vector_math_001.operation = 'DISTANCE'
    
    #node Math
    math = mpb_attributes.nodes.new("ShaderNodeMath")
    math.name = "Math"
    math.operation = 'MINIMUM'
    math.use_clamp = False
    
    #node White Noise Texture
    white_noise_texture = mpb_attributes.nodes.new("ShaderNodeTexWhiteNoise")
    white_noise_texture.name = "White Noise Texture"
    white_noise_texture.noise_dimensions = '3D'
    
    #node Attribute.004
    attribute_004 = mpb_attributes.nodes.new("ShaderNodeAttribute")
    attribute_004.name = "Attribute.004"
    attribute_004.attribute_name = "Factor"
    attribute_004.attribute_type = 'INSTANCER'
    
    
    #Set locations
    group_output.location = (561.4135131835938, 5.959369659423828)
    group_input.location = (-431.64508056640625, 0.0)
    attribute.location = (-229.92202758789062, 255.0860595703125)
    attribute_001.location = (-229.92202758789062, 81.57588195800781)
    attribute_002.location = (-227.33743286132812, -89.34476470947266)
    attribute_003.location = (-231.64508056640625, -255.0860595703125)
    vector_math.location = (67.05342864990234, -263.4277648925781)
    vector_math_001.location = (69.59786987304688, -398.5504455566406)
    math.location = (238.00621032714844, -318.4158935546875)
    white_noise_texture.location = (207.05137634277344, 258.1507568359375)
    attribute_004.location = (-230.1576690673828, -426.41845703125)
    
    #Set dimensions
    group_output.width, group_output.height = 140.0, 100.0
    group_input.width, group_input.height = 140.0, 100.0
    attribute.width, attribute.height = 140.0, 100.0
    attribute_001.width, attribute_001.height = 140.0, 100.0
    attribute_002.width, attribute_002.height = 140.0, 100.0
    attribute_003.width, attribute_003.height = 140.0, 100.0
    vector_math.width, vector_math.height = 140.0, 100.0
    vector_math_001.width, vector_math_001.height = 140.0, 100.0
    math.width, math.height = 140.0, 100.0
    white_noise_texture.width, white_noise_texture.height = 140.0, 100.0
    attribute_004.width, attribute_004.height = 140.0, 100.0
    
    #initialize mpb_attributes links
    #attribute.Fac -> white_noise_texture.Vector
    mpb_attributes.links.new(attribute.outputs[2], white_noise_texture.inputs[0])
    #vector_math_001.Value -> math.Value
    mpb_attributes.links.new(vector_math_001.outputs[1], math.inputs[1])
    #attribute_002.Vector -> vector_math.Vector
    mpb_attributes.links.new(attribute_002.outputs[1], vector_math.inputs[1])
    #vector_math.Value -> math.Value
    mpb_attributes.links.new(vector_math.outputs[1], math.inputs[0])
    #attribute_001.Vector -> vector_math.Vector
    mpb_attributes.links.new(attribute_001.outputs[1], vector_math.inputs[0])
    #attribute_003.Vector -> vector_math_001.Vector
    mpb_attributes.links.new(attribute_003.outputs[1], vector_math_001.inputs[1])
    #attribute_001.Vector -> vector_math_001.Vector
    mpb_attributes.links.new(attribute_001.outputs[1], vector_math_001.inputs[0])
    #attribute.Fac -> group_output.Index
    mpb_attributes.links.new(attribute.outputs[2], group_output.inputs[0])
    #attribute_001.Vector -> group_output.Position
    mpb_attributes.links.new(attribute_001.outputs[1], group_output.inputs[1])
    #attribute_002.Vector -> group_output.Initial Position
    mpb_attributes.links.new(attribute_002.outputs[1], group_output.inputs[2])
    #attribute_003.Vector -> group_output.Final Position
    mpb_attributes.links.new(attribute_003.outputs[1], group_output.inputs[3])
    #white_noise_texture.Value -> group_output.Random Per Instance
    mpb_attributes.links.new(white_noise_texture.outputs[0], group_output.inputs[4])
    #math.Value -> group_output.Displacement
    mpb_attributes.links.new(math.outputs[0], group_output.inputs[5])
    #attribute_004.Fac -> group_output.Factor
    mpb_attributes.links.new(attribute_004.outputs[2], group_output.inputs[6])
    
    mpb_attributes.use_fake_user = True
    
    return mpb_attributes


