'''Create a function called "fizz_buzz" which takes a number n and prints all the numbers from zero to n, replacing multiples of 3 with the string "Fizz", multiples of 5 with the string "Buzz", and multiples of both 5 and 3 with the string "FizzBuzz".

Example: If n = 15 the funtion should print 0, 1, 2, Fizz, 4, Buzz, 6, 7, 8, 9, Buzz, 11, Fizz, 13, 14, FizzBuzz'''


def fizz_buzz(n):
    i = 0
    while i < n:
        output = ''
        if not i % 3:
            output += "Fizz"
        if not i % 5:
            output += "Buzz"
        if i % 3 and i % 5:
            output = i
        print output
        i += 1
