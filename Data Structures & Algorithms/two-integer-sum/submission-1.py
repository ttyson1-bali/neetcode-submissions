class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for index ,num in enumerate(nums):
            compliment = target - num

            if compliment in seen:
                return[seen.get(compliment), index]
            
            seen[num] = index