import pygame
import sys

pygame.init()

# Window dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Platformer Game')

# Clock to control the frame rate
clock = pygame.time.Clock()



# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player settings
player_width = 50
player_height = 50
player_x = WINDOW_WIDTH // 2 - player_width // 2
player_y = WINDOW_HEIGHT - player_height
player_velocity = 5
player_jump_height = 10
player_is_jumping = False



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= player_velocity
    if keys[pygame.K_RIGHT]:
        player_x += player_velocity

    # Player jump
    if not player_is_jumping:
        if keys[pygame.K_SPACE]:
            player_is_jumping = True
    else:
        if player_jump_height >= -10:
            neg = 1
            if player_jump_height < 0:
                neg = -1
            player_y -= (player_jump_height ** 2) * 0.5 * neg
            player_jump_height -= 1
        else:
            player_is_jumping = False
            player_jump_height = 10

    # Draw everything
    window.fill(WHITE)
    pygame.draw.rect(window, BLUE, (player_x, player_y, player_width, player_height))
    pygame.display.update()

    # Frame rate
    clock.tick(60)


