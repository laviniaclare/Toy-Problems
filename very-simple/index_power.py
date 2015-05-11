'''Given an array with positive numbers and a number N find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1.

Examples:
- array = [1, 2, 3, 4] and N = 2, then the result is 3 ^ 2 == 9;
- array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.'''


def index_power(array, n):
    if n > (len(array)-1):
        return -1
    else:
        return array[n] ** n
