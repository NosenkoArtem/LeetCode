from typing import List
from random import randint

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            j = n - i
            chars = set(str(i)+str(j))
            if '0' not in chars:
                return i, j
            
solution = Solution().getNoZeroIntegers(1010)
print(solution)