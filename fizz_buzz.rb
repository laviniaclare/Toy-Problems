'''
Create a function called "fizz_buzz" which takes a number n and prints all the numbers from zero to n, replacing multiples of 3 with the string "Fizz", multiples of 5 with the string "Buzz", and multiples of both 5 and 3 with the string "FizzBuzz".

Example: If n = 15 the funtion should print 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz
'''

def fizz_buzz(n)
    (1..n).each do |n|
        value = ""
        if n % 3 != 0 and n % 5 != 0
            value = n.to_s
        end
        if n % 3 == 0
            value = "Fizz"
        end
        if n % 5 == 0
            value += "Buzz"
        end
        puts value
    end
end

fizz_buzz(20)