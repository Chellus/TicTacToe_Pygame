import pygame
import time

pygame.init()

# the window width and height is 500
window_w = 600
window_h = 600

# colors
black = (0, 0, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# fonts
end_font = pygame.font.Font('freesansbold.ttf', 120)

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

# this function returns 0 if there's no winner yet, 1 if the winner is the X and 2 if the winner is the O
def check_winner():
    global board

    # check for every row
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            if board[i][0] != 0:
                return board[i][0]

    # check for every column
    for j in range(3):
        if board[0][j] == board[1][j] and board[1][j] == board[2][j]:
            if board[0][j] != 0:
                return board[0][j]

    # check left-to-right diagonal
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] != 0:
            return board[0][0]

    # check right-to-left diagonal
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] != 0:
            return board[0][2]

    return 0

def check_draw():
    global board
    counter = 0

    for i in range(3):
        for j in range(3):
            if board[i][j] != 0:
                counter += 1

    if counter == 9:
        return True
    return False


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

# button function
def button(msg, font_size, x, y, w, h, ac, ic, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    pressed = False

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(window, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
            pressed = True
    else:
        pygame.draw.rect(window, ic, (x, y, w, h))

    smallText = pygame.font.Font('freesansbold.ttf', font_size)
    textSurf = smallText.render(msg, True, black)
    textRect = textSurf.get_rect()
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    window.blit(textSurf, textRect)
    return pressed

# main game loop
def game_loop():
    running = True
    global turn
    time.sleep(1)
    while running:

        window.fill(white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                game_quit()

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

        if check_winner() == 1:
            running = False
            winner = True

            while winner:
                window.fill(white)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        winner = False
                        break

                textSurface = end_font.render('X wins!', True, black)
                textRect = textSurface.get_rect()
                textRect.center = ((window_w / 2), (window_h / 2))
                window.blit(textSurface, textRect)
                pygame.display.update()
                clock.tick(15)

            break


        elif check_winner() == 2:
            running = False
            winner = True

            while winner:
                window.fill(white)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        winner = False
                        break

                textSurface = end_font.render('O wins!', True, black)
                textRect = textSurface.get_rect()
                textRect.center = ((window_w / 2), (window_h / 2))
                window.blit(textSurface, textRect)
                pygame.display.update()
                clock.tick(15)

            break

        if check_draw():
            running = False
            tie = True

            while tie:
                window.fill(white)

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        tie = False
                        game_quit()

                textSurface = end_font.render('Tie :(', True, black)
                textRect = textSurface.get_rect()
                textRect.center = ((window_w / 2), (window_h / 2))
                window.blit(textSurface, textRect)
                pygame.display.update()
                clock.tick(15)

            break


        pygame.display.update()
        clock.tick(30)

# start menu function
def intro():
    intro = True

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                game_quit()

        window.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 80)
        textSurf = largeText.render('Tic-Tac-Toe!', True, black)
        textRect = textSurf.get_rect()
        textRect.center = ((window_w / 2), (window_h / 3))
        window.blit(textSurf, textRect)

        if button('Play!', 30, 75, 400, 200, 100, green, bright_green, game_loop):
            intro = False
        if button('Quit', 30, 325, 400, 200, 100, red, bright_red, game_quit):
            intro = False
        pygame.display.update()
        clock.tick(30)


if __name__ == "__main__":
    intro()
