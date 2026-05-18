# @param {String} s
# @return {Boolean}
def is_valid(s)
    stack = []
    open_brackets = ["(", "{", "["]

    # for bracket in s
    s.each_char do |bracket|
        if open_brackets.include?(bracket)
            stack.push(bracket)
        
        elsif !stack.empty? && stack[-1] == "(" && bracket == ")"
            stack.pop()

        elsif !stack.empty? && stack[-1] == "[" && bracket == "]"
            stack.pop()

        elsif !stack.empty? && stack[-1] == "{" && bracket == "}"
            stack.pop()

        else
            return false
        end        
    end

    return stack.empty?

end