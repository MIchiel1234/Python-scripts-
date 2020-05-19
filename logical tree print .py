height = eval(input("enter value fot the height \n"))
row = 0
while row < height:
        count = 0
        while count < height - row:
            print(end = " ")
            count += 1
        count = 0
        while count < 2 * row +1 :
            print(end = "*")
            count += 1
        print()
        row += 1
