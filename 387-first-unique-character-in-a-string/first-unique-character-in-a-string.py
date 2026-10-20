class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq_map = dict()

        for i in range(0,len(s)):
            if s[i] in freq_map:
                freq_map[s[i]] += 1
            else:
                freq_map[s[i]] = 1

        for i in range(len(s)):
            if freq_map[s[i]] == 1:
                return i
        return -1
        


        