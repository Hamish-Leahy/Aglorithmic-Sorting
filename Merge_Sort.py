"""
merge_sort.py

Implementation of the merge sort algorithm.
"""

def merge_sort(arr):
    """
    Sorts a list in ascending order using the merge sort algorithm.
    
    Args:
        arr (list): The list of elements to be sorted.
        
    Returns:
        list: The sorted list.
        
    Example:
        >>> merge_sort([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
        [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    
    Args:
        left (list): The first sorted list.
        right (list): The second sorted list.
        
    Returns:
        list: The merged sorted list.
    """
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    
    return merged

if __name__ == "__main__":
    import doctest
    doctest.testmod()
