from collections import Counter

class Solution:
    def __init__(self):
        self.vowes = set(['a', 'e', 'i', 'o', 'u'])
    def maxFreqSum(self, s: str) -> int:
        cnt_char = Counter(s)

        freq_conson = [freq for char, freq in cnt_char.items() if char not in self.vowes]
        freq_vowes  = [freq for char, freq in cnt_char.items() if char in self.vowes]

        max_freq_conson = max(freq_conson, default=0)
        max_freq_vowels = max(freq_vowes, default=0)

        return max_freq_conson + max_freq_vowels
    

solution = Solution().maxFreqSum(""successes"")
    