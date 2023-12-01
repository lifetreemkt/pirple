
# Função para desenha o tabuleiro
def drawField():
    for row in range(5): #0,1,2,3,4
        if row % 2 == 0:
            for column in range(5):
                if column % 2 == 0:
                        if column != 4:
                            print (" ", end="")
                        else:
                            print(" ")
                else:
                    print("|", end="")     
        else:
            print("-----")

print ("Welcome to Tic Tac Toe\nThis is our battlefield:");
drawField()
#starting the game
while (True):
    MoveRow = int(input("Enter row number please:"))
    MoveColumn = int(input("Enter Column number please:"))
    if Player == 1:
        
