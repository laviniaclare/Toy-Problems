import random


def shuffle_list(input_list):
    output = []
    while len(input_list) > 1:
        length = len(input_list)
        index = random.randint(0, length-1)
        print index
        item = input_list.pop(index)
        output.append(item)
    output.append(input_list[0])
    return output


print shuffle_list([1, 2, 3, 4, 5, 6])
