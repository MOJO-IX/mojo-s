import pygame
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the game window
WINDOW_WIDTH = 300
WINDOW_HEIGHT = 300
BLOCK_SIZE = WINDOW_WIDTH // 3

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Create the game board
board = [['' for _ in range(3)] for _ in range(3)]

# Draw the grid
def draw_grid():
    for i in range(1, 3):
        pygame.draw.line(window, BLACK, (0, i * BLOCK_SIZE), (WINDOW_WIDTH, i * BLOCK_SIZE), 2)
        pygame.draw.line(window, BLACK, (i * BLOCK_SIZE, 0), (i * BLOCK_SIZE, WINDOW_HEIGHT), 2)

# Draw X and O
def draw_xo():
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(window, BLACK, (col * BLOCK_SIZE, row * BLOCK_SIZE), ((col + 1) * BLOCK_SIZE, (row + 1) * BLOCK_SIZE), 2)
                pygame.draw.line(window, BLACK, ((col + 1) * BLOCK_SIZE, row * BLOCK_SIZE), (col * BLOCK_SIZE, (row + 1) * BLOCK_SIZE), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(window, BLACK, (col * BLOCK_SIZE + BLOCK_SIZE // 2, row * BLOCK_SIZE + BLOCK_SIZE // 2), BLOCK_SIZE // 2 - 5, 2)

# Check for winner
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != '':
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]
    return None

# Main game loop
current_player = 'X'
running = True
while running:
    window.fill(WHITE)
    draw_grid()
    draw_xo()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            col = x // BLOCK_SIZE
            row = y // BLOCK_SIZE
            if board[row][col] == '':
                board[row][col] = current_player
                winner = check_winner()
                if winner:
                    print(f"Player {winner} wins!")
                    running = False
                elif all(board[i][j] != '' for i in range(3) for j in range(3)):
                    print("It's a draw!")
                    running = False
                else:
                    current_player = 'O' if current_player == 'X' else 'X'
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
