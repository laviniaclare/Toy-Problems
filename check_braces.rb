'''
Create a function that takes in an arry of strings containing brackets (ex: "[]{()}") and checks to see if they are well formed.
Return an array of the well formed examples

Well formed examples: "{([])}","[]{}()","[{}]()"
Poorly formed examples: "[{]}]","{{]]", "]()"
'''

def check_braces(braces)
    valid_braces = braces.filter_map { |braces_string|
        braces_string if valid?(braces_string)
    }
    return valid_braces
end

def valid?(braces_string)
    # If this were a class this map would go outside the function
    closing_to_openening_braces_map = {
        "}" => "{",
        "]" => "[",
        ")" => "("
    }

    open_braces = []

    # if the first brace is a closing brace the string is not well formed so we can return early
    unless closing_to_openening_braces_map.key?(braces_string[0])
        braces_string.split("").each do |brace|
            if !closing_to_openening_braces_map.key?(brace)
                open_braces.append(brace)
            elsif open_braces[-1] == closing_to_openening_braces_map[brace]
                open_braces.pop()
            else
                return false
            end
        end
    else
        return false
    end

    if open_braces.empty?
        return true
    else
        return false
    end
end

puts("All well formed -> ['{([])}','[]{}()','[{}]()']")
puts(check_braces(["{([])}","[]{}()","[{}]()"]))
puts("All poorly formed -> []")
puts(check_braces(["[{]}]","{{]]", "]()"]))
puts("Mixed -> ['{([])}','[]{}()','[{}]()']")
puts(check_braces(["[{]}]","{{]]", "]()", "{([])}","[]{}()","[{}]()"]))