class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left = 0
        right = len(nums) - 1
        curr = 0

        while curr <= right:
            if nums[curr] == 0:
                nums[curr], nums[left] = nums[left], nums[curr]
                curr += 1
                left += 1

            elif nums[curr] == 1:
                curr += 1
            else:
                nums[curr],nums[right] = nums[right],nums[curr]
                right -= 1







        
        