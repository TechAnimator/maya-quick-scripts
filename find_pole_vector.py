import pymel.core as pm
import math


# I forget where I found this function, but it isn't mine so I can't take credit

def find_pole_vector_position(nodes, angle=1, distance=1):
    """Pass three nodes and a vector will be returned. When @angle is equal to 1.0 the pole vector is perpendicular,
    @distance defaults to the length of the node's span."""
    chain_span = nodes[2].getTranslation(space='world') - nodes[0].getTranslation(space='world')
    upper_span = nodes[1].getTranslation(space='world') - nodes[0].getTranslation(space='world')
    lower_span = nodes[2].getTranslation(space='world') - nodes[1].getTranslation(space='world')
    span_length = upper_span.length() + lower_span.length()
    node_a_angle = chain_span.angle(upper_span)
    right_angle_length = math.cos(node_a_angle) * upper_span.length() * angle
    right_angle_position = nodes[0].getTranslation(space='world') + (chain_span.normal() * right_angle_length)
    pole_vector_direction = nodes[1].getTranslation(space='world') - right_angle_position
    return right_angle_position + pole_vector_direction.normal() * (span_length * distance)

# Replace hand, elbow, and uparm with your cooresponding joints/transforms you want to use
hand = pm.PyNode('L_Hand_01')
elbow = pm.PyNode('L_LowerArm_01')
uparm = pm.PyNode('L_UpperArm_01')
print find_pole_vector_position(nodes = [hand, elbow, uparm])
