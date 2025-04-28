'''
Given an array with positive numbers and a number "n" find the n-th power of the element in the array with the index n.
If n is outside of the array, then return -1.

Examples:
- array = [1, 2, 3, 4] and n = 2, then the result is 3 ^ 2 == 9;
- array = [1, 2, 3] and n = 3, but N is outside of the array, so the result is -1.
'''

def index_power(arr, n)
    if n > (arr.length - 1)
        return -1
    end

    return arr[n] ** n    
end

puts "arr=[1, 2, 3, 4], n=2 -> 9"
puts index_power([1, 2, 3, 4], 2)
puts "arr=[1, 2, 3], n=3 -> -1"
puts index_power([1, 2, 3], 3)
