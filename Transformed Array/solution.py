from typing import List

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        results = []
        for i in range(len(nums)):
            ind = (i + nums[i]) % len(nums)
            el = nums[ind]
            results.append(el)

        return results
        


results = Solution().constructTransformedArray([3,-2,1,1])
