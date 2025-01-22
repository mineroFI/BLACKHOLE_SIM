import pygame

def handle_user_input(black_hole_pos):
    mouse_x, mouse_y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:  # Si se presiona el botón izquierdo del mouse
        black_hole_pos = (mouse_x, mouse_y)
    return black_hole_pos