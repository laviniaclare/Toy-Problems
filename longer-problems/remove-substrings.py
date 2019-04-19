# removeInstances("absdefge", ["ab", "fg", "ee", "xyz"]) → sdee

#  absdefge   (ab)    -> sdefge
#  sdefge     (fg)    -> sdee
#  sdee       (ee)    -> sdee
#  sdee      (xyz)    -> sdee

import pdb

def remove_substring(input_string, substring_to_remove):
    # pdb.set_trace()
    substring_length = len(substring_to_remove)
    for i in range(len(input_string)):
        substring = input_string[i:i+substring_length]
        if substring == substring_to_remove:
            return input_string[:i] + input_string[i+substring_length:]

def removeInstances(input_string, items_to_remove):
    output = ''
    for item in items_to_remove:
        item_length = len(item)
        for i in range(len(input_string)):
            substring = input_string[i:i+item_length]
            if substring == item:
                output = input_string[:i] + input_string[i+substring_length:]
    
    return output


if __name__ == '__main__':
	
	print(removeInstances("absdefge", ["ab", "fg", "ee", "xyz"]))
