import pygame
import random

pygame.init()

width, height = 1980, 1080
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Igrca")

player_x, player_y = width // 2, height // 2
player_speed = 5

stones = [
    (random.randint(-2000, 2000), random.randint(-2000, 2000), random.randint(10, 50))
    for i in range(80)
    ]
    
running = True
clock = pygame.time.Clock()
while running:
    screen.fill((26, 36, 33))
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_y -= 5
    if keys[pygame.K_s]: player_y += 5
    if keys[pygame.K_a]: player_x -= 5
    if keys[pygame.K_d]: player_x += 5
    
    for stone in stones:
        pygame.draw.circle(screen, (128, 128, 128), (stone[0] - player_x + width // 2, stone[1] - player_y + height // 2), stone[2])   
    
    
    #player  zapomn si sihma
    pygame.draw.circle(screen, (255, 0, 0), (width // 2, height // 2), 33)
    pygame.draw.circle(screen, (255, 255, 255), (width // 2, height // 2), 30)
    
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    clock.tick(60)
    
pygame.quit()