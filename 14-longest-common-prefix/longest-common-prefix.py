class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len)
        result = ""
        for i in range(0, len(smallest)):
            for word in strs:
                if word[i] != smallest[i]:
                    return result
            result += smallest[i]
        return result


        