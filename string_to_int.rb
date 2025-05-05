'''Given a number represented as a string convert it to an integer without using "int()"'''

DIGITS_MAP = {
    "0" => 0,
    "1" => 1,
    "2" => 2,
    "3" => 3,
    "4" => 4,
    "5" => 5,
    "6" => 6,
    "7" => 7,
    "8" => 8,
    "9" => 9
}

def string_to_int(n)
    output = 0

    n.reverse!.split("").each_with_index do |digit, index|
        digit_int = DIGITS_MAP[digit]
        output += (digit_int * (10 ** index))
    end

    output
end

puts(string_to_int("123"))
puts(string_to_int("123").class)
puts(string_to_int("1000"))
puts(string_to_int("1000").class)