'''Given an iterable, called "data", and a value, remove all instences of value in data'''


def remove_all(data, value):
    edata = enumerate(data)
    value_indeces = []
    for tup in edata:
        val = tup[1]
        i = tup[0]
        if val == value:
            value_indeces.append(i)
    for i in value_indeces[::-1]:
        data.pop(i)
    return data


print(remove_all([1, 2, 4, 3, 15, 6, 2, 2], 2))
