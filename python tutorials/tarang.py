rows = int(input("Enter no of rows: "))
symbol = input("Enter symbol to use: ")

for x in range(rows):
    for y in range(0, x+1):
        print(symbol,end = "")
    print()    
