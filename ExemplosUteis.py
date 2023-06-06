# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 13:05:16 2021

@author: carlo
"""

#loop de iteração"

gameList = []
for i in range(1):
    Game = input ("Enter your favorite game: ")
    gameList.append(Game)
    
#loop true + if else
SapatosDic = {40:5 , 41:5 , 42:5}
print(SapatosDic)
while(True):
    compra = int(input("Informe o tamanho que vc quer? \n"))
    if compra < 0:
        break
    if SapatosDic[compra] > 0:
        SapatosDic[compra] -=1
    else:
        print ("fora de estoque")
    print (SapatosDic)
