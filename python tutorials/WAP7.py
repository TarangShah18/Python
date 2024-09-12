def listoftuples(n):
    output = [(i, i*i*i) for i in range (1, n+1)]
    return output

n = int(input("Enter the value of n: "))


result = listoftuples(n)

print(result)




