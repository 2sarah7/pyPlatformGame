#TODO - find some way so that the character can't go off the screen, add more platforms, add different levels and things that can kill the charater and make you have to start the level over

import pygame
import sys

#pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

#Game Variables

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
gravity_value = 5
j = 8
playerJumpHeight = j
playerIsJumping = False

#creates platforms the character moves on
platforms = [
    {"x": 0, "y": WINDOW_HEIGHT, "width": 800, "height": 10}, #base platform - necessary bc otherwise character just falls through bottom of screen
    {"x": 300, "y": 500, "width": 300, "height": 10}
]

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

    player_rect = pygame.Rect(playerX, playerY, PLAYER_WIDTH, PLAYER_HEIGHT)
    #flag to check if player is colliding with any platforms
    colliding_with_platform = False 
    
    
    #Draw platforms
    for platform in platforms: 
        pygame.draw.rect(window, WHITE, (platform["x"], platform["y"], platform["width"], platform["height"]))

    #Platform behavior
    for platform in platforms:
        platform_rect = pygame.Rect(platform["x"], platform["y"], platform["width"], platform["height"])
        
        if player_rect.colliderect(platform_rect):
            #when colliding with platform, stop falling
            playerIsJumping = False
            playerJumpHeight = j
            colliding_with_platform = True
            playerY = platform["y"] - PLAYER_HEIGHT + 2
            break
    
    
    #allows the player to jump
    if keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]:
        if not playerIsJumping:
            playerIsJumping = True
            
    if not colliding_with_platform:
        playerY += gravity_value
            
    pygame.draw.rect(window, WHITE, (playerX, playerY, PLAYER_WIDTH, PLAYER_HEIGHT))
    pygame.display.update()

    #Frame rate
    clock.tick(60)

while True:
    main()

if __name__ == "__main__":
    main()





























