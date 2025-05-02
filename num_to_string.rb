"""
Write a function, num_to_string, which takes in an integer and returns
a formatted string representation of that integer with ',' at the appropriate places.

>>> num_to_string(1234)
'1,234'

>>> num_to_string(10)
'10'

>>> num_to_string(999999)
'999,999'

"""

def num_to_formatted_string(n)
    output = ""
    n_string_reversed = n.to_s.reverse!
    counter = 0

    n_string_reversed.each_char do |digit|
        counter += 1
        if counter == 4
            output += ','
            counter = 0
        end
        output += digit
    end

    return output.reverse!
end

puts(num_to_formatted_string(1234))
puts(num_to_formatted_string(10))
puts(num_to_formatted_string(999999))
puts(num_to_formatted_string(1000000))
