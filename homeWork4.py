myUniqueList = ["orange", "apple"]
fruitName = input("Please enter a fruit name:\n")
if fruitName in myUniqueList:
    print ("fruits already on list")
else:
    myUniqueList.append(fruitName)
    print ("true - fruit added to list")

print (myUniqueList)