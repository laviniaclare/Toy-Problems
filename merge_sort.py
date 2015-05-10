def merge(list1, list2):
    output = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            output.append(list2[0])
            list2 = list2[1:]
        else:
            output.append(list1[0])
            list1 = list1[1:]
    if len(list1) > 0:
        for item in list1:
            output.append(item)
    if len(list2) > 0:
        for item in list2:
            output.append(item)
    return output


def merge_sort(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        list1 = input_list[:len(input_list)/2]
        list2 = input_list[len(input_list)/2:]
        return merge(merge_sort(list1), merge_sort(list2))


print merge_sort([3, 2, 5, 7, 1])

#sorting in reverse order


def reverse_merge(list1, list2):
    output = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] < list2[0]:
            output.append(list2[0])
            list2 = list2[1:]
        else:
            output.append(list1[0])
            list1 = list1[1:]
    if len(list1) > 0:
        for item in list1:
            output.append(item)
    if len(list2) > 0:
        for item in list2:
            output.append(item)
    return output


def reverse_merge_sort(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        list1 = input_list[:len(input_list)/2]
        list2 = input_list[len(input_list)/2:]
        return reverse_merge(reverse_merge_sort(list1), reverse_merge_sort(list2))

print "now sorting in reverse"
print reverse_merge_sort([5, 2, 4, 3, 1])
