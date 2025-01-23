import pygame
from config import WIDTH, HEIGHT, BLACK, RED, G, BLACK_HOLE_MASS
from objects import SpaceObject
# from physics import *
import random
import math
from controls import handle_user_input


icon = pygame.image.load('assets/icons/BlackHoleSIM.png')
pygame.display.set_icon(icon)


def load_music():
    pygame.mixer.init()  
    pygame.mixer.music.load('assets/music/Dreiton.mp3')
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1, 0.0)


def show_tutorial(screen):
    font = pygame.font.Font(None, 20)
    tutorial_texts = [
        "Bienvenido a BLACKHOLES_SIM!",
        "Este simulador te permite explorar cómo los agujeros negros interactúan con objetos (o algo así).",
        "",
        "Controles:",
        "Clic izquierdo: Mover el agujero negro.",
        "Clic derecho: Generar partículas.",
        "Observa cómo las partículas son absorbidas por el agujero negro.",
        "Presiona cualquier tecla para comenzar."
    ]

    y_offset = 50  # Posición inicial de la primera línea de texto
    screen.fill(BLACK)
    
    for line in tutorial_texts:
        text = font.render(line, True, (255, 255, 255))
        screen.blit(text, (50, y_offset))
        y_offset += 40  # Espacio entre líneas

    pygame.display.flip()

    # Esperar a que el jugador presione una tecla para continuar
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                waiting_for_input = False

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("BLACKHOLES_SIM")

    # Cargar y reproducir la música
    load_music()

    # Mostrar el tutorial antes de la simulación
    show_tutorial(screen)

    # Posición y características del agujero negro
    black_hole_pos = (WIDTH // 2, HEIGHT // 2)
    black_hole_radius = 20
    event_horizon_radius = black_hole_radius * 5  # El horizonte de sucesos es 5 veces el radio del agujero negro
    # rotation_angle = 0

    # Lista de objetos iniciales
    objects = [SpaceObject(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(10)]

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clic izquierdo (mover el agujero negro)
                    black_hole_pos = handle_user_input(black_hole_pos)
                elif event.button == 3:  # Clic derecho (generar partículas)
                    # Generar una nueva partícula en la posición del clic derecho
                    mouse_x, mouse_y = event.pos
                    objects.append(SpaceObject(mouse_x, mouse_y))

        
        # rotation_angle += 1  # Incrementa el ángulo de rotación
        # if rotation_angle >= 360:
        #     rotation_angle = 0

        
        black_hole_image = pygame.Surface((black_hole_radius * 2, black_hole_radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(black_hole_image, RED, (black_hole_radius, black_hole_radius), black_hole_radius)
        # rotated_black_hole = pygame.transform.rotate(black_hole_image, rotation_angle)
        # rotated_rect = rotated_black_hole.get_rect(center=black_hole_pos)
        screen.blit(black_hole_image, black_hole_image.get_rect(center=black_hole_pos))

        # Dibujar el horizonte de sucesos
        pygame.draw.circle(screen, (100, 100, 255), black_hole_pos, event_horizon_radius, 2)

        # Actualizar y dibujar objetos
        for obj in objects[:]:
            obj.move_towards_black_hole(black_hole_pos, G, BLACK_HOLE_MASS)
            obj.draw(screen)

            # Colisión con el agujero negro (desaparecen los objetos)
            dx = black_hole_pos[0] - obj.x
            dy = black_hole_pos[1] - obj.y
            distance = math.sqrt(dx**2 + dy**2)

            if distance < black_hole_radius + obj.radius: 
                objects.remove(obj)

            # Si un objeto cruza el horizonte de sucesos, cambiar comportamiento
            if distance < event_horizon_radius + obj.radius:
                obj.color = (255, 0, 0)  # Cambiar color al cruzar el horizonte

        pygame.display.flip()
        clock.tick(60)

    pygame.mixer.music.stop()  # Detener la música al finalizar
    pygame.quit()


if __name__ == '__main__':
    main()