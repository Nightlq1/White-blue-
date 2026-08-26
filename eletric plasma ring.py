import math
import pygame

pygame.init()
WIDTH, HEIGHT = 800, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Electric Plasma Ring")
clock = pygame.time.Clock()

cx, cy = WIDTH // 2, HEIGHT // 2
angle = 0
running = True

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))
    angle += 0.02

    # Outer Plasma Ring (Oscillates between pure white and bright blue)
    for i in range(180):
        a = math.radians(i * 2) + angle
        r = 170 + 12 * math.sin(i * 0.3 + angle * 6)
        x = cx + math.cos(a) * r
        y = cy + math.sin(a) * r

        # Alternates RGB values between pure white (255, 255, 255) and deep blue (30, 100, 255)
        wave = int(112 + 112 * math.sin(i * 0.2 + angle * 3))
        color = (wave, wave + 30, 255)

        pygame.draw.circle(screen, color, (int(x), int(y)), 4)

    # Electric Arcs (Bright Ice White/Blue lines)
    for i in range(40):
        a = i * 0.6 + angle * 4
        r1 = 120 + 25 * math.sin(angle * 5 + i)
        r2 = 175 + 20 * math.cos(angle * 4 + i)
        x1 = cx + math.cos(a) * r1
        y1 = cy + math.sin(a) * r1
        x2 = cx + math.cos(a + 0.25) * r2
        y2 = cy + math.sin(a + 0.25) * r2

        pygame.draw.line(
            screen, (220, 240, 255), (x1, y1), (x2, y2), 2
        )  # Soft white with a blue hint

    # Core Orbs (Deep Blue outer glow with a solid White center)
    pulse = 55 + 8 * math.sin(angle * 6)
    pygame.draw.circle(
        screen, (0, 100, 255), (cx, cy), int(pulse)
    )  # Deep royal blue outer pulse
    pygame.draw.circle(
        screen, (255, 255, 255), (cx, cy), int(pulse / 2)
    )  # Pure white core

    # Orbiting Nodes (Pure White small dots)
    for i in range(12):
        a = angle * 2 + i * (math.pi / 6)
        x = cx + math.cos(a) * 230
        y = cy + math.sin(a) * 230
        pygame.draw.circle(
            screen, (255, 255, 255), (int(x), int(y)), 5
        )  # Bright white nodes

    pygame.display.flip()

pygame.quit()