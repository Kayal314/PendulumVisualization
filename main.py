"""
Torque = moment of inertia * angular acceleration
For small angles(p) sin(p) = p
so m*g*l*p = m*l^2 * a (a = angular acceleration) {considering only magnitude}
or a = gp/l

Take each iteration of while loop as equivalent to
one unit time and update p and angular speed as necessary

The visualization is valid only for small angular displacements (approximately <= 30 degrees)
"""

import pygame
import math

pygame.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption("Pendulum Simulation")

bob = pygame.image.load("Sprites//basketball.png")
ang_speed = 0
angle = 30
acc = 0
acc_due_to_gravity = 2
length = 500
init_x = 500
init_y = 50


# line(surface, color, start_pos, end_pos, width)


def show_bob(x, y):
    screen.blit(bob, (x, y))
    x += 32
    y += 32
    pygame.draw.line(screen, (252, 119, 70), (init_x - 50, init_y), (init_x + 50, init_y), 2)
    pygame.draw.line(screen, (252, 119, 3), (init_x, init_y), (x, y), 1)


if __name__ == '__main__':
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        acc = acc_due_to_gravity * math.radians(angle) / length
        ang_speed += acc
        angle -= ang_speed
        current_x = init_x + length * math.sin(math.radians(angle))
        current_y = init_y + length * math.cos(math.radians(angle))

        show_bob(current_x, current_y)
        pygame.display.update()
