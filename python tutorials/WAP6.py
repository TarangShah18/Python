def swap(a):
    if len(a) <= 2:
        return a
    else:
        return a[0], a[1], a[-2], a[-1] 


a = input("Enter a String: ")

print(swap(a))