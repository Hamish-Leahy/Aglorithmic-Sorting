def shell_sort(arr):
    """
    Sorts a list in ascending order using the shell sort algorithm.
    
    Args:
        arr (list): The list of elements to be sorted.
        
    Returns:
        list: The sorted list.
    """
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

if __name__ == "__main__":
    arr = [12, 34, 54, 2, 3]
    print("Sorted array is:", shell_sort(arr))
