class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        length = len(nums)
        for i in range(length-2):
        # because we have two pointers l-> for left and r-> for right
            if i>0 and nums[i]==nums[i-1]:
                continue
            l = i + 1 
            r = length - 1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    # means we have to increase l by 1 
                    l = l + 1
                elif total > 0:
                    r = r - 1

                else:
                    res.append([nums[i], nums[l],nums[r]])
                    # here we are just compairing l and r so that there     will be no dublicate values
                    while l < r and nums[l]==nums[l+1]:
                        l = l + 1
                    while l < r and nums[r]==nums[r-1]:
                        r = r-1
                    l = l  + 1
                    r = r - 1
        return res


        