'''Given a number represented as a string convert it to an integer without using "int()"'''


def string_to_int(input_string):
    output = 0
    int_dict = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}
    i = 0
    for char in reversed(input_string):
        print "char", char
        index_char = i
        print "index", index_char
        digit = int_dict[char]
        print digit
        print "final:", digit * (10 ** index_char)
        output += (digit * (10 ** index_char))
        i += 1
    return output


print string_to_int('132')
print type(string_to_int('132'))
