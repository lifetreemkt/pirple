for numbers in range (101):
    if numbers % 3 == 0:
        print ("fizz")
        continue
    elif numbers % 5 == 0:
        print("buzz")
        continue
    print (numbers)