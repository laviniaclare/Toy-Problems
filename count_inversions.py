def count_inversions(sequence):
    sequence = list(sequence)
    count = 0
    i = 0
    while i < len(sequence):
        if sorted(sequence) == list(sequence):
            return count
        else:
            count = sort(sequence, count)
        i += 1
    return count


def sort(sequence, count):
    for i in range(len(sequence)-1):
        if sequence[i] > sequence[i+1]:
            count += 1
            temp = sequence[i]
            sequence[i] = sequence[i+1]
            sequence[i+1] = temp
    return count

one_inversion = count_inversions((1, 2, 3, 5, 4))
all_inverted = count_inversions((3, 2, 1))
three_inversions = count_inversions((1, 2, 5, 3, 4, 7, 6))
no_inversions = count_inversions((1, 2, 3))

print(one_inversion)
print(all_inverted)
print(three_inversions)
print(no_inversions)

assert(one_inversion == 1)
assert(all_inverted == 3)
assert(three_inversions == 3)
assert(no_inversions == 0)
