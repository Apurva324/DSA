class Solution:
    def generateParenthesis(self, n: int) -> list[str]:

        result = []
        def fun(n, open, closed, temp):
            if open == n and closed == n:
                result.append("".join(temp))
                return
#  for open 
            if open < n:
                temp.append('(')
                fun(n, open + 1, closed, temp)
                temp.pop()

# for closed
            if closed < open:
                temp.append(')')
                fun(n, open, closed + 1, temp)
                temp.pop()
        fun(n, 0, 0, [])   
        return result
            
        