string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "San", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""


def count_unique(string1):
    string = string1.strip()
    pass
print "        "
print "What are elements? Words? Chracters?"


"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists
"""


def common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return set1 & set2

print "Testing common_items:"
print common_items(list1, list2)
print "                   "


"""
Given two lists, (without using the keyword 'in' or the method 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""


def common_items2(list1, list2):
    output = []
    keys = list1
    length = len(list1)
    values = [1 for i in range(length)]
    mydict = dict(zip(keys, values))
    for item in list2:
        if item in mydict:
            output.append(item)

    return output

print "Testing common_items2:"
print common_items2(list1, list2)
print "                   "


"""
Given a list of numbers, return list of number pairs that sum to zero
"""


def sum_zero(list1):
    output = []
    mydict = {num: 'x' for num in list1}

    for key in mydict:
        if key > 0 and key * -1 in mydict:
            output.append((key, key*-1))
    return output

print "          "
print "Testing sum_zero:"
print sum_zero(list1)
print "           "


"""
Given a list of words, return a list of words with duplicates removed
"""


def find_duplicates(words):
    output = []
    for word in words:
        if not word in output:
            output.append(word)
    return output


print "Testing Q1 'find_duplicates':"
print find_duplicates(['hi', 'hi', 'hi'])
print find_duplicates(['how', 'are', 'you', 'how', 'are'])
print find_duplicates(['cool', 'beans'])
"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""


def word_length(words):
    unique_words = list(set(words))
    sorted_words = sorted(words, key=len)
    for word in sorted_words:
        print word

word_length(['yo', 'a', 'what', 'sup'])

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""


def english_2_pirate(string):
    e2pdict = {
        "sir": "matey",
        "hotel": "fleabag inn",
        "student": "swabbie",
        'boy': 'matey',
        'madam': 'proud beauty',
        'professor': 'foul blaggart',
        'restaurant': 'galley',
        'your': 'yer',
        'excuse': 'arr',
        'students': 'swabbies',
        'are': 'be',
        'lawyer': 'foul blaggart',
        'the': 'th',
        'restroom': 'head',
        'my': 'my',
        'hello': 'avast',
        'is': 'be',
        'man': 'matey'
        }
    string = string.lower()
    word_list = string.split()
    word_index = 0
    for word in word_list:
        if word in e2pdict:
            pirate_translation = e2pdict[word]
            word_list.remove(word)
            word_list.insert(word_index, pirate_translation)
        word_index += 1

    output = ' '.join(word_list)

    return output

print "Testing english_2_pirate translator"
print english_2_pirate("man, this professor needs to get off my back")
