#Create a function that takes in two parameters: rows, and columns, both of which are integers. 
#The function should then proceed to draw a playing board (as in the examples from the lectures) 
#the same number of rows and columns as specified. 
#After drawing the board, your function should return True

size = int(input("What size game board do You want? "))

def hLine (size):
    return " ---" * size + " \n"

def vColumn (size):
    return "|   " * size + "|\n"

def zBoard ( size ):
    board = ""
    for i in range(size):
        board += hLine (size)
        board += vColumn(size)
    board += hLine(size)
    return board
    return True

print(zBoard(size))
