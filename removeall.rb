'''Given an array, called "data", and a value, remove all instences of value in data'''

def remove_all(data, value)
    filtered_data = data.filter_map { |item| 
        item if item != value
    }

    filtered_data
end

puts(remove_all([1,2,1,4,3,7,1], 1))
puts(remove_all(["a", "b", "z", "c"], "z"))
puts(remove_all(["zz"], "10"))
