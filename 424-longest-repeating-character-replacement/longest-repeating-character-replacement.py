class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_length = 0
        freq = {}
        max_freq = 0

        for right in range(0,len(s)):
            # calculating frequencies 
            freq[s[right]] = freq.get(s[right], 0) + 1

            # calculating max freq
            max_freq = max(max_freq, freq[s[right]])

            while (right- left + 1) - max_freq > k:
                # invalid window
                # move left
                freq[s[left]] -= 1
                left += 1
            max_length = max(max_length, right - left + 1)

        return max_length




