class Solution:
    def isPalindrome(self, s: str) -> bool:
        


        s = [char.lower() for char in s if char.isalnum()]

        left = 0
        right = len(s) - 1
        
        while left <= len(s)-1:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
    