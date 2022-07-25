class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(len(nums) == 0): return [-1 , -1]
        a = bisect_left(nums , target)
        b = bisect_right(nums , target)
        if(a == b and ( a >= len(nums) or nums[a] != target)) : return [-1 , -1]
        return [a , b - 1]