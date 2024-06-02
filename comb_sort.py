"""
comb_sort.py

Implementation of the comb sort algorithm.
"""

def comb_sort(arr):
    """
    Sorts a list in ascending order using the comb sort algorithm.
    
    Args:
        arr (list): The list of elements to be sorted.
        
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    gap = n
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap // shrink)
        if gap <= 1:
            gap = 1
            sorted = True
        i = 0
        while i + gap < n:
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
