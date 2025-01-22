import pygame
import math
from config import WHITE

class SpaceObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 5
        self.color = WHITE
        self.speed = 0 
        self.vx = 0  # Componente x de la velocidad
        self.vy = 0  # Componente y de la velocidad
        self.original_radius = self.radius

    def move_towards_black_hole(self, black_hole_pos, G, black_hole_mass):
        dx = black_hole_pos[0] - self.x
        dy = black_hole_pos[1] - self.y
        distance = math.sqrt(dx**2 + dy**2)
        
        if distance < 1:
            return
        
        force = G * black_hole_mass / (distance**2)
        ax = force * (dx / distance)
        ay = force * (dy / distance)
        
        self.vx += ax
        self.vy += ay
        
        self.x += self.vx
        self.y += self.vy

        if distance < 100:
            self.radius = max(1, self.original_radius * (distance / 100))

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), int(self.radius))    