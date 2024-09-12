def swap(L1):
    L1[0], L1[-1] = L1[-1], L1[0]
    return L1



L1 = [1, 2, 3, 4, 5, 6, 7]

print(swap(L1))

