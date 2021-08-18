import numpy as np
import pygame
import sys

pygame.init()

# Screen Parameters (Width, Height, Line Width)
Width = 600
Height = Width
Line_Width = 15
Win_Line = 15
Square_Size = 200


# Circle
Circle_Radius = 60
Circle_Width = 15

# X line
Cross_Width = 25
Space = 55

# Board Parameters
Board_Rows = 3
Board_Cols = 3

# Color in rgb: red green blue
BG_Color = (3, 223, 252)
Line_Color = (3, 252, 119)
Circle_Color = (252, 128, 3)
X_Line_Color = (57, 252, 3)

# Play Screen
screen = pygame.display.set_mode((Width, Height))
screen.fill(BG_Color)
# name of the game in the screen
pygame.display.set_caption('Tic Tac Toe')

# Board
board = np.zeros((Board_Rows, Board_Cols))


def draw_lines():
    # (screen , Color of line, (start coordinate), (stop coordinate),Width of line )
    # 1 Horizontal
    pygame.draw.line(screen, Line_Color, (0, Square_Size), (Width, Square_Size), Line_Width)
    # 2 Horizontal
    pygame.draw.line(screen, Line_Color, (0, 2 * Square_Size), (Width, 2 * Square_Size), Line_Width)
    # 1 Vertical
    pygame.draw.line(screen, Line_Color, (Square_Size, 0), (Square_Size, Height), Line_Width)
    # 2 Vertical
    pygame.draw.line(screen, Line_Color, (2 * Square_Size, 0), (2 * Square_Size, Height), Line_Width)


def draw_figures():
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            if board[row][col] == 1:
                pygame.draw.circle(screen, Circle_Color, (int(col * Square_Size + Square_Size/2), int(row * Square_Size + Square_Size/2)), Circle_Radius, Circle_Width)
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_Line_Color, (col * Square_Size + Space, row * Square_Size + Square_Size - Space), (col * Square_Size + Square_Size - Space, row * Square_Size + Space), Cross_Width)
                pygame.draw.line(screen, X_Line_Color, (col * Square_Size + Space, row * Square_Size + Space), (col * Square_Size + Square_Size - Space, row * Square_Size + Square_Size - Space), Cross_Width)


def mark_square(row, col, player):
    board[row][col] = player


def available_square(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            if board[row][col] == 0:
                return False
    return True


def check_win(player):
    # vertical win check
    for col in range(Board_Cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player or board[2][col] == player and board[1][col] == player and board[0][col] == player:
            draw_vertical_winning_line(col, player)
            return True

    # horizontal win check
    for row in range(Board_Rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player or board[row][2] == player and board[row][1] == player and board[row][0] == player:
            draw_horizontal_winning_line(row, player)
            return True

    # asc diagonal win check
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # desc diagonal win check
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False


def draw_vertical_winning_line(col, player):
    posX = int(col * 200 + 100)

    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = X_Line_Color

    pygame.draw.line(screen, color, (posX, 15), (posX, Height - 15), Win_Line)


def draw_horizontal_winning_line(row, player):
    posY = int(row * 200 + 100)

    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = X_Line_Color

    pygame.draw.line(screen, color, (15, posY), (Height - 15, posY), Win_Line)


def draw_asc_diagonal(player):
    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = X_Line_Color

    pygame.draw.line(screen, color, (15, Height - 15), (Width - 15, 15), Win_Line)


def draw_desc_diagonal(player):
    if player == 1:
        color = Circle_Color
    elif player == 2:
        color = X_Line_Color

    pygame.draw.line(screen, color, (15, 15), (Width - 15, Height - 15), Win_Line)


def restart():
    screen.fill(BG_Color)
    draw_lines()
    player = 1
    for row in range(Board_Rows):
        for col in range(Board_Cols):
            board[row][col] = 0


draw_lines()

player = 1
game_over = False

# main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

            mouseX = event.pos[0]  # x

            mouseY = event.pos[1]  # y

            clicked_row = int(mouseY // 200)

            clicked_col = int(mouseX // 200)

            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1

        draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                game_over = False
    pygame.display.update()