def countingSort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # There are 10 possible digits (0-9)

    # Count the occurrences of each digit at the current place value
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Calculate the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    # Copy the output array to the original array
    for i in range(n):
        arr[i] = output[i]

def radixSort(arr):
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit, using place value (exp)
    exp = 1
    while max_num // exp > 0:
        countingSort(arr, exp)
        exp *= 10  # Move to the next place value

# Example usage:
array = [170, 45, 75, 90, 802, 24, 2, 66]
radixSort(array)
print("Sorted array:", array)

