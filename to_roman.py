'''Given a number convert it to a Roman numeral string'''


def to_roman(num):
    roman = ''
    roman_dict = {'1': 'I', '5': 'V', '10': 'X', '50': 'L', '100': 'C', '500': 'D', '1000': 'M'}
    num_string = str(num)
    digit_list = list(num_string)
    print num
    print digit_list
    if len(digit_list) >= 4:
        roman += (roman_dict['1000']*int(digit_list[0]))
        digit_list = digit_list[1:]
        print digit_list
        print roman
    if len(digit_list) == 3:
        curr_digit = int(digit_list[0])
        if curr_digit >= 5:
            roman += roman_dict['500']
            curr_digit -= 5
        roman += (roman_dict['100']*curr_digit)
        digit_list = digit_list[1:]
        print digit_list
        print roman
    if len(digit_list) == 2:
        curr_digit = int(digit_list[0])
        if curr_digit >= 5:
            roman += roman_dict['50']
            curr_digit -= 5
        roman += (roman_dict['10']*curr_digit)
        digit_list = digit_list[1:]
        print digit_list
        print roman
    if len(digit_list) == 1:
        curr_digit = int(digit_list[0])
        if curr_digit >= 5:
            roman += roman_dict['5']
            curr_digit -= 5
        roman += (roman_dict['1']*curr_digit)
        print digit_list
        print roman
    print roman
    return roman

print to_roman(1652)
