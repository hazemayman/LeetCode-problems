class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_array = sorted(nums)
        answer = []
        for i in nums:
            index = bisect_left(sorted_array , i)
            answer.append(index)
            del sorted_array[index]
        return answer
                