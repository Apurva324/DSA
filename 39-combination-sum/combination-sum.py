class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        n = len(candidates)

        def func(idx, ans, total):
            if total == target:
                res.append(ans.copy())
                return
            
            if total > target:
                    return 

            for i in range(idx,n):
                ans.append(candidates[i])
                total += candidates[i]
                func(i, ans, total)
                total -= candidates[i]
                ans.pop()

        func(0, [], 0)
        return res
                    

        