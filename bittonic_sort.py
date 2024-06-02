"""
bitonic_sort.py

Implementation of the bitonic sort algorithm.
"""

def comp_and_swap(arr, i, j, dir):
    if (dir == 1 and arr[i] > arr[j]) or (dir == 0 and arr[i] < arr[j]):
        arr[i], arr[j] = arr[j], arr[i]

def bitonic_merge(arr, low, cnt, dir):
    if cnt > 1:
        k = cnt // 2
        for i in range(low, low + k):
            comp_and_swap(arr, i, i + k, dir)
        bitonic_merge(arr, low, k, dir)
        bitonic_merge(arr, low + k, k, dir)

def bitonic_sort_recursive(arr, low, cnt, dir):
    if cnt > 1:
        k = cnt // 2
        bitonic_sort_recursive(arr, low, k, 1)
        bitonic_sort_recursive(arr, low + k, k, 0)
        bitonic_merge(arr, low, cnt, dir)

def bitonic_sort(arr, up=True):
    """
    Sorts a list in ascending order using the bitonic sort algorithm.
    
    Args:
        arr (list): The list of elements to be sorted.
        up (bool): True for ascending order, False for descending order.
        
    Returns:
        list: The sorted list.
    """
    bitonic_sort_recursive(arr, 0, len(arr), 1 if up else 0)
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
