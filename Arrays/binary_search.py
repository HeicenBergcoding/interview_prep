# Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
# The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 

def search_insert(nums, target):
        # set pointers for low and high
        low, high = 0, len(nums) - 1

        # run loop until high is greater than equal to low
        while low <= high:
            # find mid positon
            mid = (low + high) // 2
            # if mid is target return it
            if nums[mid] == target:
                return mid  # Target found
            # if target is greater than mid element
            # change the low pointer to mid + 1
            elif nums[mid] < target:
                low = mid + 1  # Adjust low pointer
            # else change high pointer to mid - 1
            else:
                high = mid - 1  # Adjust high pointer

        return low