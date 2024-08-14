from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for cnt, el_1 in enumerate(nums):
            if target - el_1 in lookup:
                return [lookup[target -el_1], cnt]
            lookup[el_1] = cnt