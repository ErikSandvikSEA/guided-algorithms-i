# returns either the index of a target in the arr or, if target isn't found, return -1 
def binary_search(arr, target):
    # 1.) compare the target element to the midpoint
        # how do we fid the midpoint? what do we need to know?
        # the length of the array could help us 
        # the 'range': if we have the left-most index and the right-most index, then the midpoint element is (right + left) // 2 
    # 2.) determine which half to go in, toss out the other half
    # 3.) if the midpoint element matches our target, then we've found what we're looking for, return the midpoint index 