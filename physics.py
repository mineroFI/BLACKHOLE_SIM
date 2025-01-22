import math

def gravity_force(distance, G, black_hole_mass): # G = 1e-3, black_hole_mass = 1e6
    """ Calcula la fuerza de gravedad entre el objeto y el agujero """
    return G * black_hole_mass / (distance ** 2)

def update_velocity(position, velocity, black_hole_pos, G, black_hole_mass):
    """ Actualiza la velocidad del objeto basado en la gravedad del agujero"""
    dx = black_hole_pos[0] - position[0]
    dy = black_hole_pos[1] - position[1]
    distance = math.sqrt(dx**2 + dy**2)
    
    force = gravity_force(distance, G, black_hole_mass)
    ax = force * (dx / distance)
    ay = force * (dy / distance)
    
    velocity[0] += ax
    velocity[1] += ay
    return velocity

def update_position(position, velocity):
    """ Actualiza la posición del objeto basado en su velocidad """
    position[0] += velocity[0]
    position[1] += velocity[1]
    return position