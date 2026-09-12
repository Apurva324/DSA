class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []

        for x in nums:
            if x >= 0:
                pos.append(x)
            else:
                neg.append(x)

        if len(pos) == 0:
            return [x * x for x in neg][::-1]

        if len(neg) == 0:
            return [x * x for x in pos]

        neg = [x * x for x in neg][::-1]
        pos = [x * x for x in pos]

        n = len(neg)
        m = len(pos)

        res = []

        i = j = 0

        while i < n and j < m:
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1

        while i < n:
            res.append(neg[i])
            i += 1

        while j < m:
            res.append(pos[j])
            j += 1

        return res