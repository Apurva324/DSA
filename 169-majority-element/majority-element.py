class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]  
        
        freq_map = {}
        n = len(nums)
        
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1
        
        # Find element that appears more than n/2 times
        for num, count in freq_map.items():
            if count > n // 2:
                return num