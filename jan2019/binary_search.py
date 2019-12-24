from typing import List

def binary_search(sorted_array: List[int], target: int) -> int:
    """
    Args: 
        sorted_array (list) - a sorted array A of n integers such that A_0 <= A_1 <= A_2 . . . A_{n-1} 
        target (int) - an integer value to search for in the array
    Returns:
        the index of target in sorted_array
    """
    left_bound = 0
    right_bound = len(sorted_array) - 1
    while left_bound <= right_bound:
        idx_mid = (left_bound + right_bound) // 2
        if sorted_array[idx_mid] < target:
            left_bound = idx_mid + 1
        elif sorted_array[idx_mid] > target:
            right_bound = idx_mid - 1
        else:
            return(idx_mid)
    return(-1)


def test_binary_search():
    test1 = ([1,2,3,4,5,6], 5, 4) # n = 6, target (5) right of idx_mid
    test2 = ([1,2,3,4,5,6], 2, 1) # n = 6, target (2) left of idx_mid
    test3 = ([1,2,3,4,5,6], 1, 0) # n = 6, target (1) on left end
    test4 = ([1,2,3,4,5,6], 6, 5) # n = 6, target (6) on right end
    test5 = ([1,2,3,4,5,6], 12, -1) # n = 6, target (12) not in array
    test6 = ([1,2,3,4,6,7,10], 7, 5) # n = 7, target (7) right of idx_mid
    test7 = ([1,2,3,4,6,7,10], 2, 1) # n = 7, target (2) left of idx_mid
    test8 = ([1,2,3,4,6,7,10], 4, 3) # n = 7, target (4) at idx_mid
    test9 = ([1,2,3,4,6,7,10], 1, 0) # n = 7, target (1) at left end
    test10 = ([1,2,3,4,6,7,10], 10, 6) # n = 7, target (10) at right end
    test11 = ([1,2,3,4,6,7,10], 12, -1) # n = 7, target (12) not in array

    all_tests = [test1, test2, test3, test4, test5, test6,
                    test7, test8, test9, test10, test11]
    
    passed = 0
    for i in all_tests:
        sorted_array, target, expected = i
        actual = binary_search(sorted_array, target)
        print(f'input: {sorted_array}')
        print(f'target: {target}')
        print(f'expected: {expected}')
        print(f'actual: {actual}')
        if actual == expected:
            print('test passed')
            passed += 1
        else:
            print('test failed')
        print('\n')
    
    print(f'{passed} of 11 tests passed')


test_binary_search()


