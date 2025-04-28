'''
Write a function, is_even, which takes an integer k and returns True if k is even and False if k is odd.
You cannot use multiplication, divison, or the modulo opperator
'''

def is_even?(k)
    num = k
    while num > 0
        num = num - 2
    end

    if num == 0
        return true
    else
        return false
    end
end

puts("0:", is_even?(0))
puts("2:", is_even?(2))
puts("3:", is_even?(3))
puts("10:", is_even?(10))
puts("13:", is_even?(13))