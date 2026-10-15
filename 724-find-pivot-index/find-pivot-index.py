class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = 0
        left = 0

        for i in range(0, len(nums)):
            total += nums[i]

        for i in range(0, len(nums)):
            right = total - nums[i] - left

            if left == right:
                return i

            left+= nums[i]

        return - 1



