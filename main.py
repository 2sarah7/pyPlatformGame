import pygame
import sys

#pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 800
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Platformer Game")

PLAYER_WIDTH = 20
PLAYER_HEIGHT = 20
playerX = WINDOW_HEIGHT // 2 - PLAYER_WIDTH // 2
playerY = WINDOW_HEIGHT - PLAYER_HEIGHT
player_vel = 5
j = 8
playerJumpHeight = j
playerIsJumping = False


def main():
    global playerX, playerY, playerJumpHeight, playerIsJumping

    #Quits pygame when told to
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        playerX -= player_vel
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        playerX += player_vel

    #Player jump
    #playerIsJumping - says if player is currently jumping, checks if player is not, then they can jump
    if not playerIsJumping:
        #When key is pressed, playerIsJumping says that the player is currently jumping and cannot innitate another jump until it is finished
        if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
            playerIsJumping = True
            #Becuae it is true, the code now runs the else block
    else:
        #Makes the character jump in a positive direction until at playerJumpHeight
        if playerJumpHeight >= -j:
            neg = 1
            if playerJumpHeight < 0:
                neg = -1
            #Creates parabloic jump trajectory and neg controls direction (up or down)
            playerY -= (playerJumpHeight  ** 2) * 0.5 * neg
            playerJumpHeight -= 1
        else:
            #Once jump is done, playerIsJumping is set to false again
            playerIsJumping = False
            playerJumpHeight = j
    
    #Draw everything
    window.fill(BLUE)
    pygame.draw.rect(window, WHITE, (playerX, playerY, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.display.update()

    #Frame rate
    clock.tick(60)

while True:
    main()

if __name__ == "__main__":
    main()





























