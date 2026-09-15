class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        result = []
        curr_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            curr_sum += nums[right]

            while curr_sum >= target:
                 min_length = min(min_length, right - left + 1)
                 curr_sum = curr_sum - nums[left]
                 left += 1
        
        if min_length == float('inf'): # means we did not find any subarray which is equal to or greater than target that's why we get - infinity
            return 0

        return min_length


        




        