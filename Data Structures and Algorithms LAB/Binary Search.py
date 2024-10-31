# Function to perform Merge Sort
def merge_sort(arr):
    # Base condition for recursion: return if list has only one element
    if len(arr) > 1:
        # Split the array into left and right halves
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        # Recursively call merge_sort on each half
        merge_sort(left_arr)
        merge_sort(right_arr)

        # Initialize pointers for left, right, and merged arrays
        i = 0  # Pointer for left array
        j = 0  # Pointer for right array
        k = 0  # Pointer for merged array

        # Merge the two halves
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
            else:
                arr[k] = right_arr[j]
                j += 1
            k += 1

        # Add any remaining elements from left_arr
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # Add any remaining elements from right_arr
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


# Function to perform Radix Sort
def radix_sort(a):
    num = 0
#---------------------------------------------------------------------------------------
    # Find the largest value in the array
    max = a[0]
    for x in a:
        if x > max:
            max = x   # Update max with the largest value found
#---------------------------------------------------------------------------------------
    # Determine the number of digits in the largest number
    while max > 0:
        num += 1
        max = max / 10  # Dividing by 10 to count each digit
#---------------------------------------------------------------------------------------
    # Initialize B as a 3D array with 10 sub-lists (for each digit place 0-9)
    for x in range(0, num):
        B = [[] for _ in range(10)]  # Create 10 slots for each digit 0-9
        for number in a:
            temp = number // 10**x % 10  # Extract relevant digit based on place value
            B[temp].append(number)       # Add number to the correct slot

        # Flatten the sorted sections in B back into array a
        i = 0
        for x in range(0, 10):
            for j in range(len(B[x])):
                a[i] = B[x][j]
                i += 1
#---------------------------------------------------------------------------------------

# Function to perform Quick Sort
def quick_sort(arr, left, right):
    if left < right:
        # Get the partitioning position
        partison_pos = partison(arr, left, right)
        # Recursively apply quick sort to each partition
        quick_sort(arr, left, partison_pos - 1)
        quick_sort(arr, partison_pos + 1, right)

# Helper function to find the partition position for Quick Sort
def partison(arr, left, right):
    i = left
    j = right - 1
    pivot = arr[right]  # Choose the rightmost element as pivot

    # Loop until pointers meet
    while i < j:
        # Increment left pointer if the element is less than pivot
        while i < right and arr[i] < pivot:
            i += 1
        # Decrement right pointer if the element is greater than or equal to pivot
        while j > left and arr[j] >= pivot:
            j -= 1
        # Swap elements if the pointers haven't crossed
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Swap pivot element to its correct position
    if arr[i] > pivot:
        arr[i], arr[right] = arr[right], arr[i]

    return i


# Sample array for testing
array_1 = [45, 112, 232, 31, 53, 731, 121, 22, 42]

# Testing Quick Sort
print("Real array: " + str(array_1))
quick_sort(array_1, 0, len(array_1) - 1)
print("Sorted with Quick Sort: " + str(array_1))
