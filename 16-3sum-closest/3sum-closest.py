class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range(0,len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
               curr_sum = nums[i] + nums[left] + nums[right]

            # Exactly matched
               if curr_sum == target:
                 return curr_sum

            # Updating 
               if abs(target - curr_sum) < abs(target - closest_sum):
                  closest_sum = curr_sum

            #  Moving pointers
               if curr_sum < target:
                 left += 1
               else:
                right -= 1

        return closest_sum
            
             






            
