class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        low = 0
        high = len(nums) -1 
        first = -1 

        while low <= high:
            mid = (low + high)// 2
            if (nums[mid] < target):
                low = mid + 1
            elif (nums[mid] > target):
                high = mid - 1
            else: # target == nums[mid]
                first = mid
                high = mid - 1 # for first occurence

        # for the last occurnce
        low = 0
        high = len(nums) -1 
        last = -1 

        while low <= high:
            mid = (low + high)// 2
            if (nums[mid] < target):
                low = mid + 1
            elif (nums[mid] > target):
                high = mid - 1
            else: # target == nums[mid]
                last = mid
                low = mid + 1
        return [first, last]


