class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq_map = dict()
        for i in range(0, len(s)):
            if s[i] in freq_map:
                freq_map[s[i]] += 1
            else:
                freq_map[s[i]] = 1
        odd = False
        res = 0
        for char in freq_map:
            if freq_map[char] % 2 == 0:
                res += freq_map[char]
            else:
                odd = True
            
        if odd == False: # means that all the char in the list have even number of char
            return res

        for char in freq_map:
            if freq_map[char] % 2 == 1:
                res += freq_map[char] - 1
        return res + 1

