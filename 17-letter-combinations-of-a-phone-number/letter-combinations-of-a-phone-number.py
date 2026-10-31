class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []
        idx = 0
        n = len(digits)
        def func(n, idx, diary):
            if idx == n:
                res.append("".join(diary))
                return
            choice = phone[digits[idx]] 
            for j in range(0, len(choice)): # we are trying to loop in 2 then 3
                diary.append(choice[j])
                func(n, idx+1, diary)
                diary.pop()

        if n == 0:
            return []

        func(n, idx, [])

        return res





        