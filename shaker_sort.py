"""
cocktail_shaker_sort.py

Implementation of the cocktail shaker sort algorithm.
"""

def cocktail_shaker_sort(arr):
    """
    Sorts a list in ascending order using the cocktail shaker sort algorithm.
    
    Args:
        arr (list): The list of elements to be sorted.
        
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end, start, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True
        start = start + 1
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
