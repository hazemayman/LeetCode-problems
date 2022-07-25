class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        lookup  = {}
        for i in nums:
            if i in lookup:
                del lookup[i]
            else:
                lookup[i] = None
        for key in lookup:
            return key