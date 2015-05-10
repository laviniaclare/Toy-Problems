'''reversing a list in place'''


def reverse_list(input_list):
    for i in range(len(input_list)/2):
        temp = input_list[-(i+1)]
        input_list[-(i+1)] = input_list[i]
        input_list[i] = temp
    print input_list

reverse_list([1, 2, 3, 4, 5])
reverse_list([1, 2, 3, 4])
