def reverse_int(x: int) -> int:
    def reverse_positive_int(x:int) -> int:
        return(int("".join(list(str(x))[::-1])))
    def check_if_32_bit(x:int) -> int:
        if x in range((-1 << 31),(1 << 31)-1):
            return(x)
        else:
            return(0)

    if x < 0:
        x *= -1
        reversed_int = -1 * reverse_positive_int(x)
        return(check_if_32_bit(reversed_int))
    else:
        reversed_int = reverse_positive_int(x)
        return(check_if_32_bit(reversed_int))

print(reverse_int(-532))
print(reverse_int(1534236469))