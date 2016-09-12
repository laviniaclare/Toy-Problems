"""Write a function, num_to_string, which takes in an integer and returns
 a string representation of that integer with ',' at the appropriate 
 groupings to indicate thousands places.

>>> num_to_string(1234)
'1,234'

>>> num_to_string(10)
'10'

>>> num_to_string(999999)
'999,999'

"""


def num_to_string(num):
    output = ''
    # convert num to string
    num_string = str(num)
    counter = 0
    # for digit in number string (loop from end, reverse direction)
    for digit in reversed(num_string):
        # if the number is a multiple of 3 from the end add comma
        if not counter % 3 and not counter == 0 and not digit == "-":
            output += ','
        # always add the digit
        output += digit
        counter += 1

    # return final number string
    return output[::-1]

if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
