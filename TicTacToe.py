from tkinter import S
from tkinter.tix import ROW
from turtle import color
import pygame, sys
import numpy as numpy

pygame.init()

# Constant variables
HEIGHT = 600
WIDTH = 600
FILL_COLOR = (44, 124, 230)
LINE = (38, 59, 112)
display = pygame.display.set_mode((WIDTH, HEIGHT) )
ROWS = 3
COLS = 3
SIZE = WIDTH // COLS


# Circle Dimensions
CIR_RADIUS = SIZE//3
CIR_WIDTH = 15
CIR_COLOR = (64, 247, 2)

# X Dimensions
SPACE = SIZE//4
X_WIDTH = 25
X_COLOR = (212, 0, 0)




# Add title to the game
pygame.display.set_caption("Tic Tac Toe")

# Add color to the screen
display.fill(FILL_COLOR)

# Create board
board = numpy.zeros((ROWS, COLS))

# Utility Functions
def spot(row, column, person):
    board[row][column] = person

def is_empty(row, column):
    if(board[row][column]) == 0:
        return True
    else:
        return False

def is_full():
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == 0:
                return False
    return True


# Lines
def lines():
    # Creating Horizontal Bars 
    pygame.draw.line(display, LINE, (20, SIZE), (WIDTH-30, SIZE), 15)
    pygame.draw.line(display, LINE, (20, 2*SIZE), (WIDTH-30, 2*SIZE), 15)

    # Creating Vertical Lines
    pygame.draw.line(display, LINE, (SIZE, 20), (SIZE, HEIGHT-30), 15)
    pygame.draw.line(display, LINE, (SIZE*2, 20), (SIZE*2, HEIGHT-30), 15)
lines()


def markTheBoard():
	for row in range(ROWS):
		for col in range(COLS):
			if board[row][col] == 1:
				pygame.draw.circle( display, CIR_COLOR, (int( col * SIZE + SIZE//2 ), int( row * SIZE + SIZE//2 )), CIR_RADIUS, CIR_WIDTH )
			elif board[row][col] == 2:
				pygame.draw.line( display, X_COLOR, (col * SIZE + SPACE, row * SIZE + SIZE - SPACE), (col * SIZE + SIZE - SPACE, row * SIZE + SPACE), X_WIDTH )	
				pygame.draw.line( display, X_COLOR, (col * SIZE + SPACE, row * SIZE + SPACE), (col * SIZE + SIZE - SPACE, row * SIZE + SIZE - SPACE), X_WIDTH )


def win(player):
    for column in range(COLS):
        if board [0][column] == player and board[1][column] == player and board[2][column] == player:
            verticalLine(column, player)
            return True
        
    for row in range(ROWS):
        if board [row][0] == player and board[row][1] == player and board[row][2] == player:
            horizontalLine(row, player)
            return True

    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        diagDLine(player)
        return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        diagALine(player)
        return True
    
    return False    


        

def verticalLine(column, player):
	x = column * SIZE + SIZE//2

	if player == 1:
		color = CIR_COLOR
	elif player == 2:
		color = X_COLOR

	pygame.draw.line(display, color, (x, 15), (x, HEIGHT - 15), 15 )

    

def horizontalLine(row, player):
	y = row * SIZE + SIZE//2

	if player == 1:
		color = CIR_COLOR
	elif player == 2:
		color = X_COLOR

	pygame.draw.line(display, color, (15, y), (WIDTH - 15, y), 15 )
 

def diagALine(player):
	if player == 1:
		color = CIR_COLOR
	elif player == 2:
		color = X_COLOR

	pygame.draw.line( display, color, (15, HEIGHT - 15), (WIDTH - 15, 15), 15 )


def diagDLine(player):
	if player == 1:
		color = CIR_COLOR
	elif player == 2:
		color = X_COLOR

	pygame.draw.line(display, color, (15, 15), (WIDTH - 15, HEIGHT - 15), 15 )




player = 1
winner = False
# Main working loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not winner:
            # Gets x y coordinates of where the mouse clicked
            X = event.pos[0]
            Y = event.pos[1]

            # Allows for coverage of the whole square
            clickedRow = int(Y // SIZE)
            clickedCol = int(X // SIZE)

            if is_empty(clickedRow, clickedCol):
                spot(clickedRow, clickedCol, player)
                if win(player):
                    winner = True
                player = player % 2 + 1
                print(board)
                markTheBoard()

        

    pygame.display.update()