"""
Given a string to format and a dictionary with formatting information return a string
return a string with the proper HTML formatting applied. 

The keys of the format dictionary represent the html format tag (ex: 'b', 'u', 'i'), and the values
are a list of lists, each inner list containing a start and end index that the format shoudl be applied to.
Index ranges are inclusive of the start and exclusive of the end.

Tags should be properly closed and formats can overlap.

Example input:
format_dict: {'b':[[0, 2], [5, 8]], 'i':[[1, 4]]}
string: 'asdfghg'
output: '<b>a<i>s</i></b><i>df</i>g<b>hg</b>'

"""

def main(format_dict, input_string):
	"""Formats a string given the specifications in the foramt dictionary"""
	pass



if __name__ == '__main__':
	format_dict = {'b':[[0, 2], [5, 8]], 'i':[[1, 4]]}
	input_string = 'asdfghg'
	expected_output = '<b>a<i>s</i></b><i>df</i>g<b>hg</b>'

	actual_output = main(format_dict, input_string)

	print(actual_output)
	# assert actual_output == expected_output
