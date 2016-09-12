'''Given a number convert it to a Roman numeral string'''


def to_roman(num):
    roman = ''
    roman_dict = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M'}
    num_string = str(num)

    if len(num_string) >= 4:
        roman += (roman_dict['1000']*int(num_string[0]))
        num_string = num_string[1:]

    if len(num_string) == 3:
        curr_digit = int(num_string[0])
        if curr_digit >= 5:
            roman += roman_dict['500']
            curr_digit -= 5
        roman += (roman_dict['100']*curr_digit)
        num_string = num_string[1:]

    if len(num_string) == 2:
        curr_digit = int(num_string[0])
        if curr_digit >= 5:
            roman += roman_dict['50']
            curr_digit -= 5
        roman += (roman_dict['10']*curr_digit)
        num_string = num_string[1:]

    if len(num_string) == 1:
        curr_digit = int(num_string[0])
        if curr_digit >= 5:
            roman += roman_dict['5']
            curr_digit -= 5
        roman += (roman_dict['1']*curr_digit)

    return roman


print to_roman(1652)
