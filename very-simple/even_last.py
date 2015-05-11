'''Given an array of integers, find the sum of the elements with even indexes (0th, 2nd, 4th...) then multiply this summed number and the final element of the array together.

For an empty array, the result will always be 0 (zero).

Examples: even_last([0, 1, 2, 3, 4, 5]) --> 30
          even_last([1, 3, 5]) --> 30
          even_last([6]) --> 36
          even_last([]) --> 0
'''


def even_last(array):
    if len(array) == 0:
        return 0
    else:
        evens = [array[i] for i in range(len(array)) if not i % 2]
        return sum(evens) * array[-1]
