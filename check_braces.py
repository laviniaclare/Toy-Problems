'''Create a function that takes in some strings containing brackets (ex: "[]{()}") and checks to see if they are well formed.
print 1 for each string that is well formed and zero for each one that isn't.

Well formed examples: "{([])}","[]{}()","[{}]()"
Poorly formed examples: "[{]}]","{{]]", "]()"'''


def check_braces(expressions):
    for string in expressions:
        if is_balanced(string):
            print(1)
        else:
            print(0)


def is_balanced(string):
    closure_dict = {'{': '}', '[': ']', '(': ')'}
    open_braces = []
    for char in string:
        if char in closure_dict or len(open_braces) == 0:
            open_braces.append(char)
        elif closure_dict[open_braces[-1]] == char:
            open_braces.pop()
    if len(open_braces) == 0:
        return True
    else:
        return False

check_braces([")(){}", "[]({})", "([])", "{()[]}", "([)]"])
