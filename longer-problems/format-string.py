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

def map_index_to_format(format_dict, num_indexes):
	"""Takes in a dictionary which maps formats to index ranges
	and flips it to map indexes to formats"""
	output = {i: [] for i in range(num_indexes+1)}

	for format_tag in format_dict:
		for index_range in format_dict[format_tag]:
			start = index_range[0]
			end = index_range[1]
			output[start].append('<'+format_tag+'>')
			output[end].append('<'+format_tag+'/>')

	return output



def main(format_dict, input_string):
	"""Formats a string given the specifications in the foramt dictionary"""
	formatted_string = ''
	index_to_format_map = map_index_to_format(format_dict, len(input_string))
	open_tags = []
	for i in range(len(input_string)):
		tags = index_to_format_map[i]

		if not open_tags:
			for tag in tags:
				open_tags.append(tag)
				formatted_string += tag
		else:
			for tag in tags:
				if tag[-2] == '/':
					import pdb; pdb.set_trace()
					reopen = []
					# find location in open tags
					index_opened = open_tags.index(tag.replace('/',''))
					# figure out which tags need to be closed before current tag can close
					for open_tag in open_tags[index_opened::-1]:
						reopen.append(open_tag)
						formatted_string += open_tag[:-2]+'/'+open_tag[-2:]
					formatted_string += tag
					# reopen tags which should not be closed
					for tag in reopen:
						formatted_string += tag
				else:
					# TODO: reduce repitition
					open_tags.append(tag)
					formatted_string += tag
		
		formatted_string += input_string[i]

	return formatted_string



if __name__ == '__main__':
	format_dict = {'b':[[0, 2], [5, 7]], 'i':[[1, 4]], 'u':[[1, 5]]}
	input_string = 'asdfghg'
	expected_output = '<b>a<i><u>s</i></b><i>df</i>g</u><b>hg</b>'

	actual_output = main(format_dict, input_string)

	print(actual_output)
	# assert actual_output == expected_output
