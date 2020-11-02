import pygame

pygame.init()

# the window width and height is 500
window_w = 600
window_h = 600

# colors
white = (255, 255, 255)
black = (0, 0, 0)

# create the window and the clock
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

#Set caption
pygame.display.set_caption("TicTacToe - Pygame")

# this function is called after the user closes the window
def game_quit():
    pygame.quit()
    quit()

# main game loop
def game_loop():
    running = True

    while running:

        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # tic-tac-toe grid
        pygame.draw.line(window, black, (200, 0), (200, 600), 3)
        pygame.draw.line(window, black, (400, 0), (400, 600), 3)
        pygame.draw.line(window, black, (0, 200), (600, 200), 3)
        pygame.draw.line(window, black, (0, 400), (600, 400), 3)

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    # start the game loop
    game_loop()
    # after the game loop is finished, quit the game
    game_quit()
