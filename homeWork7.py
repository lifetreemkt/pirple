FavoriteDic = {"My favorite song is":"Wasted Years" , "Recorded by":"Iron Maiden" , "It was released in":"1986"}
print("Are you interested in knowing my favorite song?\n")
question = str(input("Answer Yes or No\n")).capitalize()
if question == "Yes":
    for x, y in FavoriteDic.items():
        print (x,y)
elif question == "No":
    print ("Ok, no problem")
else:
    print ("I did not understand your answer...")
