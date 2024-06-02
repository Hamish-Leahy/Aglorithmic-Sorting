def insertion_sort(arr):
    """
    Sorts an array using insertion sort algorithm.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
if __name__ == "__main__":
    data = [5, 2, 8, 12, 1, 6]
    insertion_sort(data)
    print(f"Sorted array: {data}")
