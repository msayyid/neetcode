def merge_sort(arr):
    # base case: when do we stop?
    if len(arr) <= 1:
        return arr # we must return arr not none, otherwise things break
    
    # find the middle to split
    mid = len(arr) // 2

    # recursively sort the left half
    sorted_left = merge_sort(arr[:mid])
    
    # recursively sort the right half
    sorted_right = merge_sort(arr[mid:])
    
    # merge the two sorted halves and return
    return merge(sorted_left, sorted_right)



def merge(A, B):
    result = []
    i, j = 0, 0
    
    # main loop: both have elements
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            result.append(A[i])
            i += 1
        else:
            result.append(B[j])
            j += 1

    while i < len(A):
        result.append(A[i])
        i += 1
    
    while j < len(B):
        result.append(B[j])
        j += 1
    
    return result

print(merge_sort([5, 2, 8, 1, 9, 3]))
# Expected: [1, 2, 3, 5, 8, 9]

print(merge_sort([1]))
# Expected: [1]

print(merge_sort([3, 1]))
# Expected: [1, 3]

print(merge_sort([4, 4, 2, 2, 1]))
# Expected: [1, 2, 2, 4, 4]