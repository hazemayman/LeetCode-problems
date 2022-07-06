class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        duplicates = 0
        i = 0
        while(i < len(nums)):
            compare = nums[i]
            if(duplicates):
                temp = nums[i - duplicates]
                nums[i - duplicates] = nums[i]
                nums[i] = temp
            j = i
            while j+1< len(nums) and compare == nums[j+1]:
                j+=1
                duplicates+=1
            i = j+1
        return len(nums) - duplicates
            