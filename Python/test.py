def longest_increasing_subsequence(array: list) -> list:
    n = len(array)

    if n <= 1:
        return array
    
    pivot = array[0]
    is_found = False
    i = 1
    longest_subseq = []
    while not is_found and i < n:
        if array[i] < pivot:
            is_found = True
            a += len(array[i:])
            temp_array = [element for element in array[i:] if element >= array[i]]
            temp_array = longest_increasing_subsequence(temp_array)
            if len(temp_array) > len(longest_subseq):
                longest_subseq = temp_array
        else:
            i += 1

    temp_array = [element for element in array[1:] if element >= pivot]
    temp_array = [pivot, *longest_increasing_subsequence(temp_array)]
    if len(temp_array) > len(longest_subseq):
        return temp_array
    else:
        return longest_subseq

print(longest_increasing_subsequence([10, 22, 9, 33, 21, 50, 41, 60, 80]))