class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
# Checking
        while (left<right):
            width = right - left 
            ht = min(height[left],height[right])
            curr_water = width * ht
            max_water = max(curr_water,max_water)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water


        

