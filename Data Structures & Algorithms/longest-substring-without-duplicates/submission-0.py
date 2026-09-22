class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        cur = ""

        for char in s:
            if char not in cur:
                cur += char
                longest = max(longest, len(cur))
            else:
                cur = cur[cur.index(char)+1:]
                cur += char
        
        return longest

