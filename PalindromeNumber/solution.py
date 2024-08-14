class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0) or (x % 10 == 0 and x != 0):
            return False

        reverted_x = 0
        while x > reverted_x:
            reverted_x = reverted_x * 10 + x % 10
            x = x // 10
        return (reverted_x == x) or (x == reverted_x // 10)