import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
running = True
dt : float = 0

player_position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT  event means the user clicked x to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    pygame.draw.circle(screen,"red",player_position,40)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_position.y -= 300 * dt
    if keys[pygame.K_s]:
        player_position.y += 300 * dt
    if keys[pygame.K_a]:
        player_position.x -= 300* dt
    if keys[pygame.K_d]:
        player_position.x += 300 * dt
    
    # flip() the display to put your work on screen
    pygame.display.flip()

    # Limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate.
    # independent physics.
    dt = clock.tick(60) / 1000



pygame.quit()
