class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        lookup = [None] * len(nums)
        maxArrayScore = None
        maxArrayScoreIndex = None
        for i in range(len(nums)):
            if(maxArrayScore == None):
                maxArrayScore = nums[i]
                maxArrayScoreIndex = i
                lookup[i] = nums[i]
            else:
                if(maxArrayScoreIndex < i - k):
                    window = lookup[0 if i-k < 0 else i-k : i]
                    print(window)
                    maxIndex = -1
                    maxScoreInner = window[0]
                    for j in range(len(window)):
                        if(window[j] >= maxScoreInner):
                            maxIndex = j
                            maxScoreInner = window[j]
                    maxArrayScore = maxScoreInner
                    maxArrayScoreIndex = i - k + maxIndex

                lookup[i] = nums[i] + maxArrayScore 

                if(nums[i] + maxArrayScore >= maxArrayScore):
                    maxArrayScore = nums[i] + maxArrayScore 
                    maxArrayScoreIndex = i

        print(lookup)
        return lookup[-1]
