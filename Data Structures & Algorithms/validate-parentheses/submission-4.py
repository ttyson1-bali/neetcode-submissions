class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []

        if len(s) % 2 != 0:
            return False

        for char in s:
            if char not in pairs:
                stack.append(char)
            elif len(stack) == 0 or stack[-1] != pairs[char]:
                return False
            else:
                stack.pop()

        return len(stack) == 0