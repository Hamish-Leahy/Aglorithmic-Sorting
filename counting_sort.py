def counting_sort(arr):
    """
    Sorts a list in ascending order using the counting sort algorithm.
    
    Args:
        arr (list): The list of elements to be sorted.
        
    Returns:
        list: The sorted list.
    """
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m                
    for a in arr:
        count[a] += 1            
    i = 0
    for a in range(m):            
        for c in range(count[a]):  
            arr[i] = a
            i += 1
    return arr

if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    print("Sorted array is:", counting_sort(arr))
