def binary_search(x, l):
    L = sorted(l)
    if len(L) == 1:
        if L[0] == x:
            return True
        else:
            return False
    else:
        L1 = L[:len(L)/2]
        L2 = L[len(L)/2:]
        if L1[-1] == x:
            return True
        elif L1[-1] > x:
            return binary_search(x, L1)
        elif L2[0] == x:
            return True
        elif L2[0] < x:
            return binary_search(x, L2)
    return False


print binary_search(3, [1, 4, 2, 3])
print binary_search(5, [1, 2, 4, 5, 6, 4, 7])
print binary_search(10, [1, 2, 3])
print binary_search(1, [1])
