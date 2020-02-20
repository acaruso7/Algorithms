def isPalindrome(x:int) -> bool:
    reverse = list(str(x))[::-1]
    if str(x) == "".join(reverse):
        return(True)
    else:
        return(False)

