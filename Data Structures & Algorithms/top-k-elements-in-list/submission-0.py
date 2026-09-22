class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen = {}

        for n in nums:
            seen[n] = seen.get(n,0) + 1

        seen = sorted(seen, key = seen.get, reverse = True)
        return seen[:k]