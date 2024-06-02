# Algorithmic Sorting

This repository contains implementations of various sorting algorithms in Python. The current implementations include:

- [Insertion Sort](#insertion-sort)
- [Merge Sort](#merge-sort)

## Insertion Sort

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

### Usage

To use the insertion sort implementation, you can import the `insertion_sort` function from the `insertion_sort.py` file:

```python
from insertion_sort import insertion_sort

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = insertion_sort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

### Example

You can also run the script directly to see the sorting in action:

```bash
python insertion_sort.py
```

This will run the built-in doctests to verify the implementation.

## Merge Sort

Merge sort is an efficient, stable, comparison-based, divide and conquer sorting algorithm. Most implementations produce a stable sort, which means that the order of equal elements is the same in the input and output.

### Usage

To use the merge sort implementation, you can import the `merge_sort` function from the `merge_sort.py` file:

```python
from merge_sort import merge_sort

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_arr = merge_sort(arr)
print(sorted_arr)  # Output: [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
```

### Example

You can also run the script directly to see the sorting in action:

```bash
python merge_sort.py
```

This will run the built-in doctests to verify the implementation.

## Running Tests

Both sorting algorithms come with built-in doctests. To run the tests, execute the respective Python files:

```bash
python insertion_sort.py
python merge_sort.py
```

If the tests pass, there will be no output. If any tests fail, the doctest module will provide details on the failed cases.

## Contributing

Contributions are welcome! If you have suggestions for improvements or additional sorting algorithms to include, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
