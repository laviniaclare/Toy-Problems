'''
Given an array of integers, find the sum of the elements with even indexes (0th, 2nd, 4th...)
then multiply this summed number and the final element of the array together.

For an empty array, the result will always be 0 (zero).

Examples: even_last([0, 1, 2, 3, 4, 5]) --> 30
          even_last([1, 3, 5]) --> 30
          even_last([6]) --> 36
          even_last([]) --> 0
'''

def even_last(arr)
    output = 0
    if arr.empty?
        return output
    end
    
    arr.each_with_index do |num, i|
        if i % 2 == 0
            output += num
        end
    end
    
    return output * arr.last()
end

puts "Input is: [0, 1, 2, 3, 4, 5]"
puts "Output is:", even_last([0, 1, 2, 3, 4, 5])
puts "Input is []"
puts "Output is:", even_last([])
puts "input is [6]"
puts "Output is:", even_last([6])
puts "Input is [1, 3, 5]"
puts "Output is:", even_last([1, 3, 5])
