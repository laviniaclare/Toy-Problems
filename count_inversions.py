def count_inversions(sequence):
    sequence = list(sequence)
    count = 0
    i = 0
    while i < len(sequence):
        print i
        if sorted(sequence) == list(sequence):
            return count
        else:
            print sequence
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

count_inversions((1, 2, 3, 5, 4))
count_inversions((3, 2, 1))
count_inversions((1, 2, 5, 3, 4, 7, 6))
