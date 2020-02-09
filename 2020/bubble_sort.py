from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Args:
        arr (List[int]): unsorted array of integers
    Returns:
        List[int]: sorted array of integers (ascending)
    """
    for i in range(0, len(arr)-1):
        swapped = False
        for j in range(0, len(arr)-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                swapped = True
        if not swapped:
            break
    return(arr)
        



def test_bubble_sort():
    test1 = ([4,3,2,1,1,4,3], [1,1,2,3,3,4,4])
    test2 = ([5,4,3,2,1], [1,2,3,4,5])
    test3 = ([5,-1,0,4,3,5,-6,-6,0,10], [-6,-6,-1,0,0,3,4,5,5,10])

    all_tests = [test1, test2, test3]
    
    passed = 0
    for i in all_tests:
        unsorted_array, expected = i
        actual = bubble_sort(unsorted_array)
        print(f'input: {unsorted_array}')
        print(f'expected: {expected}')
        print(f'actual output: {actual}')
        if actual == expected:
            print('test passed')
            passed += 1
        else:
            print('test failed')
        print('\n')
    
    print(f'{passed} of {len(all_tests)} tests passed')


test_bubble_sort()

