def dict(n):
    dict2 = {x : x * x for x in range(1, n+1)}
    return dict2

n = int(input("Enter a number: "))

result = dict(n)
print(result)


