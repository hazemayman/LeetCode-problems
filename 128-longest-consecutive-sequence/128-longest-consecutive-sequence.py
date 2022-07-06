class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        a = set(nums)
        streak = 0
        for number in a:
            if(number-1 in a):
                continue
            
            mini = 1
            while number+1 in a:
                number+=1
                mini+=1
            streak = max(streak , mini)
            
        return streak 