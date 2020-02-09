# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# EXAMPLES:
# Input: "()"
# Output: true

# Input: "()[]{}"
# Output: true

# Input: "(]"
# Output: false

# Input: "([)]"
# Output: false

# Input: "{[]}"
# Output: true

def isValid(s: str) -> bool:
    if s == "":
        return(True)
    else:
        stack = []
        pairs = {")":"(", "}":"{", "]":"["}
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            elif char in [")", "}", "]"]:
                if len(stack)>0 and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return(False)
        if len(stack) > 0:
            return(False)
        return(True)



def test_is_valid():
    test1 = "()"
    test2 = "()[]{}"
    test3 = "(]"
    test4 = "{[[]{}]}"
    test5 = "{[}]"
    test6 = "]"
    test7 = "[])"
    assert isValid(test1) == True
    assert isValid(test2) == True
    assert isValid(test3) == False
    assert isValid(test4) == True
    assert isValid(test5) == False
    assert isValid(test6) == False
    assert isValid(test7) == False
    print('all tests passed')

test_is_valid()

