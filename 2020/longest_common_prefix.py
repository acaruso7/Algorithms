from typing import List

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:
# Input: ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

def lcp(strs: List[str]) -> str:
    if strs == []:
        return("")
    shortest_string = min(map(lambda x: len(x), strs))
    j = 0
    longest_common_prefix = ""
    prefixes = []
    while True:
        for i in strs:
            prefixes.append(i[j]) if len(i) >= 1 else prefixes.append("")
        if len(set(prefixes)) > 1:
            return(longest_common_prefix)
        else:
            if len(strs[0]) >= 1:
                longest_common_prefix += strs[0][j]
            else:
                longest_common_prefix += ""
        prefixes = []
        j += 1
        if j >= shortest_string:
            return(longest_common_prefix)



assert lcp(["flower","flow","flight"]) == "fl"
assert lcp(["dog","racecar","car"]) == ""
assert lcp(['aaa', 'aa', 'aa']) == "aa"
assert lcp(["",""]) == ""
assert lcp([]) == ""
assert lcp([""]) == ""
