# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. 
# This is consistent to C's strstr() and Java's indexOf().

def strStr(haystack:str, needle:str) -> int:
    if needle not in haystack:
        return(-1)
    elif needle == "" or needle == haystack or haystack[0] == needle:
        return(0)
    else:
        substring_length = len(needle)
        additional_idxs = [i+1 for i in range(substring_length-1)]
        for idx, val in enumerate(haystack[:-(substring_length-1)]):
            chars = [haystack[idx]] + [haystack[idx+i] for i in additional_idxs]
            this_substring = "".join(chars)
            if this_substring == needle:
                return(idx)
        
print(strStr('helloooo', 'ello')) #idx of first occurrence = 1

