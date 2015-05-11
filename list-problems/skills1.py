'''Write a function that takes a list of numbers and returns a new list with only the odd numbers.'''


def all_odd(some_list):
    #using a for-loop
    output = []
    for item in some_list:
        if item % 2:
            output.append(item)
    return output

print "testing all_odd:"
print all_odd([1, 2, 3, 4, 5, 6, 7])
print all_odd([1, 5, 3, 4, 8, 6, 7, 2, 3])
print all_odd([2, 4, 6, 8])


def all_odd2(input_list):
    #One line solution using list comprehnsion
    return [x for x in input_list if x % 2]

print "testing all_odd2:"
print all_odd2([1, 2, 3, 4, 5, 6, 7])
print all_odd2([1, 5, 3, 4, 8, 6, 7, 2, 3])
print all_odd2([2, 4, 6, 8])


'''Write a function that takes a list and returns a new list with only the even numbers.'''


def all_even(some_list):
    #using for-loop
    output = []
    for item in some_list:
        if not int(item) % 2:
            output.append(item)
    return output

print "testing all_even:"
print all_even([1, 2, 3, 4, 5, 6, 7, 8])
print all_even([1, 3, 5, 7])
print all_even([2, 4, 6, 8])


def all_even2(input_list):
    #using list comprehension
    return [x for x in input_list if not x % 2]


'''Write a function that takes a list of strings and returns a new list with all strings of length 4 or greater.'''


def long_words(word_list):
    #using a for-loop
    output = []
    for word in word_list:
        if len(word) >= 4:
            output.append(word)
    return output

print "testing long_words:"
print long_words(['hi', 'sup?', 'yo', 'yee', 'hyphy', "f'sho"])


def long_words2(words):
    #using a list comprehension
    return [word for word in words if len(word) >= 4]

print "testing long_words2:"
print long_words2(['hi', 'sup?', 'yo', 'yee', 'hyphy', "f'sho"])


'''Write a function that finds the smallest element in a list of integers and returns it.'''


def smallest(some_list):
    output = some_list[0]
    for i in some_list:
        if i < output:
            output = i
    return output

print "testing smallest:"
print smallest([1, 2, 3, 4, 5])
print smallest([7, 6, 5, 4, 3, 2])
print smallest([42, 3, 55, 4, 7])


'''Write a function that finds the largest element in a list of integers and returns it.'''


def largest(some_list):
    output = some_list[0]
    for elem in some_list:
        if elem > output:
            output = elem
    return output


print"testing largest:"
print largest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print largest([2, 4, 3, 1, 6, 5, 9])
print largest([8, 5, 6, 4, 3, 7, 2])
print largest([-5, -3, -2])


'''Write a function that takes a list of numbers and returns a new list of all those numbers divided by two.'''


def halvesies(some_list):
    #using a for-loop
    output = []
    for number in some_list:
        half = number/2.0
        output.append(half)
    return output

print "now testing halvesies:"
print halvesies([-4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def halvesies2(input_list):
    #using a list comprehension
    return [x/2.0 for x in input_list]

print "now testing halvesies2:"
print halvesies([-4, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

'''Write a function that takes a list of words and returns a list of all the lengths of those words.'''


def word_lengths(word_list):
    #using a for-loop
    output = []
    for word in word_list:
        length = len(word)
        output.append(length)
    return output

print "now testing word_lengths:"
print word_lengths(['i', 'hi', 'bye'])


def word_lengths2(words):
    #using a list comprehension
    return [len(word) for word in words]


'''Write a function (using iteration) that sums all the numbers in a list.'''


def sum_numbers(numbers):
    i = 0
    for number in numbers:
        i += number
    return i

print "now testing sum_numbers:"
print sum_numbers([1])
print sum_numbers([1, 4, -3])
print sum_numbers([-8, 10, 1])


'''Write a function that multiplies all the numbers in a list together.'''


def mult_numbers(numbers):
    i = 1
    for number in numbers:
        i = i*number
    return i

print "now testing mult_numbers:"
print mult_numbers([3, 3, 3])
print mult_numbers([1, 4, 3, 6, 8, 3, 7, 0])
print mult_numbers([10, 2, 5])


'''Write a function that joins all the strings in a list together (without using the join method) and returns a single string.'''


def join_strings(string_list):
    output = ''
    for word in string_list:
        output = output + word + ' '
    return output

print "now testing join_strings"
print join_strings(['did', 'it', 'work?'])


'''Write a function that takes a list of integers and returns the average (without using the avg method)'''


def average(numbers):
    length = 0
    for number in numbers:
        length += 1

    output = sum_numbers(numbers)/length
    return output

print "testing average:"
print average([5, 4, 6, 3, 7, 2, 8, 1, 9])
