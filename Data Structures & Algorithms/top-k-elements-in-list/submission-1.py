class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}

        for n in nums:
            seen[n] = seen.get(n,0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for key, value in seen.items():
            buckets[value].append(key)

        ans = []
        for x in range(len(buckets)-1, -1, -1):
            if len(ans) >= k:
                return ans
            ans += buckets[x]
    
