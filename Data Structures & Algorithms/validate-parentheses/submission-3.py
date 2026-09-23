class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for n in s:
            if n == ")":
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop(-1)
                else:
                    return False

            elif n == "}":
                if len(stack) > 0 and stack[-1] == "{":
                    stack.pop(-1)
                else:
                    return False

            elif n == "]":
                if len(stack) > 0 and stack[-1] == "[":
                    stack.pop(-1) 
                else:
                    return False                  
            else:
                stack.append(n)

        return (len(stack) == 0)