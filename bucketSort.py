def bucket_sort(arr):
    if len(arr) == 0:
        return arr


    min_val = min(arr)
    max_val = max(arr)


    range_val = max_val - min_val


    num_buckets = len(arr)
    buckets = [[] for _ in range(num_buckets)]


    for num in arr:

        index = int((num - min_val) / range_val * (num_buckets - 1))
        print(index)
        buckets[index].append(num)


    for i in range(len(buckets)):
        insertion_sort(buckets[i])


    sorted_array = [num for bucket in buckets for num in bucket]

    return sorted_array

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


input_array = [3,9,5,8,244]
sorted_array = bucket_sort(input_array)
print(sorted_array)
