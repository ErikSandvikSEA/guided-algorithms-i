# returns either the index of a target in the arr or, if target isn't found, return -1
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    # 1.) compare the target element to the midpoint
    while low <= high:
        # how do we fid the midpoint? what do we need to know?
        # the length of the array could help us
        # the 'range': if we have the left-most index and the right-most index, then the midpoint element is (right + left) // 2
        mid = low + high // 2
        # 2.) determine which half to go in, toss out the other half
        # reassign either the left or right index to point to the element directly next to the midpoint
        if target == arr[mid]:
            return mid
        # 3.) if the midpoint element matches our target, then we've found what we're looking for, return the midpoint index
        elif target < arr[mid]:
            high = mid - 1

        else:
            low = mid + 1
    # 4.) repeat this process: we need to loop this
    # what's our looping criteria? what tells us that we're done looping?
    # if we see that low and high are referring to the same index, and the element at that idex is not the target, then we can conclude the target isn't in the array
    return -1
