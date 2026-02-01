from typing import List

class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = [(-1)**i*(i//2 + 1) for i in range(n)]
        if n%2 == 1:
            answer[-1] = 0
        return answer
    
class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = list(range(1-n, n, 2))
        return answer