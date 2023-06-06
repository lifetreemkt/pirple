
def drawField():
    for row in range(5): #0,1,2,3,4
        if row % 2 == 0:
            for column in range(5):
                if column % 2 == 0:
                        if column !=4:
                            print (" ", end="")
                        else:
                            print(" ")
                else:
                    print("|", end="")     
        else:
            print("-----")

drawField()            