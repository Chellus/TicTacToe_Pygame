import pygame

pygame.init()

# the window width and height is 500
window_w = 600
window_h = 600

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

# create the window and the clock
window = pygame.display.set_mode((window_w, window_h))
clock = pygame.time.Clock()

# board of the game, 0 means the space is empty, 1 means there's an X in it and 2 means there's an O in it
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

# variable to know if X or O is playing, 1 = X and 2 = O
turn = 1

#Set caption
pygame.display.set_caption("TicTacToe - Pygame")

# this function is called after the user closes the window
def game_quit():
    pygame.quit()
    quit()

#function to draw the board onto the window
def draw_board():
    global board

    for y in range(0, 600, 200):
        for x in range(0, 600, 200):
            if board[x // 200][y // 200] == 1:
                pygame.draw.line(window, red, ((x + 180), (y + 10)), ((x + 10), (y + 180)), 5)
                pygame.draw.line(window, red, ((x + 10), (y + 10)), ((x + 180), (y + 180)), 5)
            elif board[x // 200][y // 200] == 2:
                pygame.draw.circle(window, blue, (x + 100, y + 100), 75, 5)

# main game loop
def game_loop():
    running = True
    global turn
    while running:

        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        # tic-tac-toe grid
        pygame.draw.line(window, black, (200, 0), (200, 600), 10)
        pygame.draw.line(window, black, (400, 0), (400, 600), 10)
        pygame.draw.line(window, black, (0, 200), (600, 200), 10)
        pygame.draw.line(window, black, (0, 400), (600, 400), 10)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # we're using this nested for loop to check if the user pressed in one of the options to play their turn
        for y in range(0, 600, 200):
            for x in range(0, 600, 200):
                # if the cursor is inside one of the buttons
                if x + 200 > mouse[0] > x and y + 200 > mouse[1] > y:
                    if click[0] == 1:
                        if turn == 1:
                            if board[x // 200][y // 200] == 0:
                                board[x // 200][y // 200] = turn
                                turn = 2
                        else:
                            if board[x // 200][y // 200] == 0:
                                board[x // 200][y // 200] = turn
                                turn = 1

        draw_board()

        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    # start the game loop
    game_loop()
    # after the game loop is finished, quit the game
    game_quit()
