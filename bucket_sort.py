def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def bucket_sort(arr):
    """
    Sorts a list in ascending order using the bucket sort algorithm.
    
    Args:
        arr (list): The list of elements to be sorted.
        
    Returns:
        list: The sorted list.
    """
    bucket = []
    slot_num = 10
    for i in range(slot_num):
        bucket.append([])
    for j in arr:
        index_b = int(slot_num * j)
        bucket[index_b].append(j)
    for i in range(slot_num):
        bucket[i] = insertion_sort(bucket[i])
    k = 0
    for i in range(slot_num):
        for j in range(len(bucket[i])):
            arr[k] = bucket[i][j]
            k += 1
    return arr

if __name__ == "__main__":
    arr = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    print("Sorted array is:", bucket_sort(arr))
