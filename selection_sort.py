def selection_sort(arr):
    # iterate through the array
    for i in range(len(arr)):
        boundary = i
        # `smallest` is the smallest element in the unsorted portion
        smallest_value = arr[boundary]
        smallest_index = boundary

        # finding the smallest element in the unsorted part of the array
        for unsorted_index in range(boundary, len(arr)):
            if arr[unsorted_index] < smallest_value:
                smallest_value = arr[unsorted_index]
                smallest_index = unsorted_index

        # once it's found, swap it with the element on the right edge of the sorted portion
        arr[boundary], arr[smallest_index] = arr[smallest_index], arr[boundary]

    return arr


arr = [5, 55, 6, 67, 16, 9, 25, 43, 12]

print(selection_sort(arr))
