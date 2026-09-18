class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        min_window_size = float('inf')
        min_window = ""

        # Frequency map for t
        freq_map_t = {}

        for i in range(0, len(t)):
            if t[i] in freq_map_t:
                freq_map_t[t[i]] += 1
            else:
                freq_map_t[t[i]] = 1

        # Frequency map for current window
        freq_map_s = {}

        for right in range(0, len(s)):

            # Add character to current window
            if s[right] in freq_map_s:
                freq_map_s[s[right]] += 1
            else:
                freq_map_s[s[right]] = 1

            # Check if window is valid
            valid = True

            for key in freq_map_t:

                if key not in freq_map_s:
                    valid = False
                    break

                if freq_map_s[key] < freq_map_t[key]:
                    valid = False
                    break

            # If valid, try to shrink the window
            while valid:

                window_size = right - left + 1

                if window_size < min_window_size:
                    min_window_size = window_size
                    min_window = s[left:right + 1]

                # Remove left character
                freq_map_s[s[left]] -= 1
                left += 1

                # Check if window is still valid
                valid = True

                for key in freq_map_t:

                    if key not in freq_map_s:
                        valid = False
                        break

                    if freq_map_s[key] < freq_map_t[key]:
                        valid = False
                        break

        return min_window