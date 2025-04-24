def bubble_sort(arr):
    """
    Bubble Sort: A simple sorting algorithm that repeatedly steps through the list,
    compares adjacent elements, and swaps them if they are in the wrong order.

    Time Complexity:
        - Best Case (already sorted): O(n)
        - Worst/Average Case: O(n^2)
    Space Complexity: O(1) (in-place sorting)
    """
    n = len(arr)  # Length of the array
    for i in range(n):
        # Flag to check if the list is already sorted
        swapped = False

        # The largest element "bubbles up" to the end of the array in each iteration
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no two elements were swapped, the array is already sorted
        if not swapped:
            break


# Example usage
# numbers = [64, 34, 25, 12, 22, 11, 90]
# print("Original array:", numbers)
# bubble_sort(numbers)
# print("Sorted array:", numbers)


def selection_sort(arr):
    """
    Selection Sort: A simple comparison-based sorting algorithm. It divides the array
    into two parts: sorted and unsorted. Repeatedly selects the smallest element
    from the unsorted part and moves it to the sorted part.

    Time Complexity:
        - Best, Worst, and Average Case: O(n^2)
    Space Complexity: O(1) (in-place sorting)
    """
    n = len(arr)  # Length of the array

    for i in range(n):
        # Assume the first element of the unsorted part is the smallest
        min_index = i

        # Find the actual smallest element in the unsorted part
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update the index of the smallest element

        # Swap the found smallest element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]


# Example usage
# numbers = [64, 25, 12, 22, 11]
# print("Original array:", numbers)
# selection_sort(numbers)
# print("Sorted array:", numbers)


def insertion_sort(arr):
    """
    Insertion Sort: A sorting algorithm that builds the sorted array one element at a time.
    It picks elements from the unsorted part and places them in the correct position in the sorted part.

    Time Complexity:
        - Best Case (nearly sorted): O(n)
        - Worst/Average Case: O(n^2)
    Space Complexity: O(1) (in-place sorting)
    """
    n = len(arr)  # Length of the array

    for i in range(1, n):  # Start with the second element
        key = arr[i]  # Element to be placed in the sorted part
        j = i - 1

        # Move elements of the sorted part that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Place the key in its correct position
        arr[j + 1] = key


# Example usage
# numbers = [12, 11, 13, 5, 6]
# print("Original array:", numbers)
# insertion_sort(numbers)
# print("Sorted array:", numbers)





"""
Extra note from Hamed:
This YT Vid does a very good job of going through this code:
https://www.youtube.com/watch?v=Vtckgz38QHs
"""

def quick_sort(array, start, end):
    """
    QuickSort implementation using the Lomuto Partition Scheme.
    - Pivot is chosen as the last element of the array or subarray.

    Args:
        array (list): The array to be sorted.
        start (int): The starting index of the subarray.
        end (int): The ending index of the subarray.

    Time Complexity:
        - Best Case: O(n log n), when partitions are balanced.
        - Average Case: O(n log n), expected for random data.
        - Worst Case: O(n^2), when partitions are highly unbalanced (e.g., already sorted array).

    Space Complexity:
        - O(log n) due to the recursion stack (best case with balanced partitions).
        - O(n) in the worst case with unbalanced partitions.
    """
    if start >= end:
        return  # Base case: single element or empty subarray is already sorted

    # Partition the array and get the pivot index
    pivot_index = partition(array, start, end)

    # Recursively apply QuickSort to the left and right subarrays
    quick_sort(array, start, pivot_index - 1)
    quick_sort(array, pivot_index + 1, end)


def partition(array, start, end):
    """
    Partition the array using the last element as the pivot.
    - Elements smaller than the pivot are placed to its left.
    - Elements greater than the pivot are placed to its right.

    Args:
        array (list): The array to partition.
        start (int): The starting index of the subarray.
        end (int): The ending index of the subarray.

    Returns:
        int: The index of the pivot after partitioning.
    """
    pivot = array[end]  # Choose the last element as the pivot
    i = start - 1  # Initialize the boundary for elements smaller than the pivot

    # Iterate through the subarray
    for j in range(start, end):
        if array[j] < pivot:  # If the current element is smaller than the pivot
            i += 1  # Move the boundary to the right
            array[i], array[j] = array[j], array[i]  # Swap elements

    # Place the pivot in its correct position
    i += 1
    array[i], array[end] = array[end], array[i]

    return i  # Return the pivot index


# Example usage
# numbers = [8, 2, 5, 3, 9, 4, 7, 6, 1]
# print("Original array:", numbers)
# quick_sort(numbers, 0, len(numbers) - 1)
# print("Sorted array:", numbers)


def merge_sort(arr):
    """
    Recursive Merge Sort: A divide-and-conquer algorithm that splits the array
    into halves, recursively sorts each half, and then merges the sorted halves.

    Time Complexity:
        - Best, Worst, and Average Case: O(n log n)
    Space Complexity: O(n) due to temporary arrays during merging.
    """

    # Base Case: An array of size 0 or 1 is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    # Step 2: Merge the two sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merge two sorted arrays into one sorted array.
    """
    merged = []
    i = j = 0

    # Compare elements from both halves and build the merged array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Append any remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Example usage
# numbers = [38, 27, 43, 3, 9, 82, 10]
# print("Original array:", numbers)
# sorted_numbers = merge_sort(numbers)
# print("Sorted array:", sorted_numbers)
