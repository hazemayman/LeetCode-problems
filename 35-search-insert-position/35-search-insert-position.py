class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        minimum = 0
        maximum = len(nums)-1 
        while(maximum >= minimum):
            middle = (maximum+minimum)//2
            if(nums[middle] == target):return middle
            if(nums[middle]>target): maximum = middle - 1
            if(nums[middle]<target) : minimum = middle + 1
        if(minimum > maximum): return maximum + 1
        else: return minimum + 1
        