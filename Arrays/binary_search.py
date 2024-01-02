# Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.
# The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(log N). 
class Solution:
    def search_insert(nums, target):
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = (low + high) // 2

            if nums[mid] == target:
                return mid  # Target found
            elif nums[mid] < target:
                low = mid + 1  # Adjust low pointer
            else:
                high = mid - 1  # Adjust high pointer

        return low