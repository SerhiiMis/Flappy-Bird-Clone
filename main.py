import pygame
import random


pygame.init()

WIDTH, HEIGHT = 400, 600
BIRD_X, BIRD_Y = 50, 300
GRAVITY = 0.5
JUMP_STRENGTH = -10
PIPE_WIDTH = 70
PIPE_GAP = 150
PIPE_SPEED = 3
FPS = 30

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird Clone")

bird = pygame.Rect(BIRD_X, BIRD_Y, 30, 30)
velocity = 0

pipes = []
def create_pipe():
    height = random.randint(100, 400)
    pipes.append(pygame.Rect(WIDTH, height, PIPE_WIDTH, HEIGHT - height))
    pipes.append(pygame.Rect(WIDTH, 0, PIPE_WIDTH, height - PIPE_GAP))

create_pipe()

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            velocity = JUMP_STRENGTH
    
    velocity += GRAVITY
    bird.y += velocity
    
    if bird.y > HEIGHT - 30:
        bird.y = HEIGHT - 30
        velocity = 0  
    
    for pipe in pipes:
        pipe.x -= PIPE_SPEED
    
    if pipes[0].x < -PIPE_WIDTH:
        pipes.pop(0)
        pipes.pop(0)
        create_pipe()
    
    pygame.draw.rect(screen, BLUE, bird)
    for pipe in pipes:
        pygame.draw.rect(screen, GREEN, pipe)
    
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()