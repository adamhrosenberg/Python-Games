import pygame

if (__name__ == "__main__"):
    pygame.init()
    window_size = window_width, window_height = 640, 480
    gameWindow = pygame.display.set_mode(window_size)

    running = 1

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = 0
