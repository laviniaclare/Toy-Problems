'''
Write a function, is_even, which takes an integer k and returns True if k is even and False if k is odd.
You cannot use multiplication, divison, or the modulo opperator
'''


def is_even(k):
    num = k
    while num > 1:
        num = num-2
    if num == 0:
        return True
    else:
        return False


print("is_even(2):", is_even(2))
print("is_even(3):", is_even(3))
print("is_even(10):", is_even(10))
print("is_even(13):", is_even(13))
