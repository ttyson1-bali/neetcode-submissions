class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        total = 1
        for x in nums:
            total *= x
            prefix.append(total)

        suffix = [0] * len(nums)
        total = 1
        for x in range(len(nums)-1, -1 , -1):
            total *= nums[x]
            suffix[x] = total
    
        ans = []
        for x in range(len(nums)):
            if x  == 0:
                ans.append(suffix[1])
            elif(x == len(nums) - 1):
                ans.append(prefix[-2])
            else:
                ans.append(prefix[x - 1] * suffix[x + 1])
        return ans
        
    
