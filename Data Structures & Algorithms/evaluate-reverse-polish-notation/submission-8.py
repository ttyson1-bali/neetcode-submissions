class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        
        for x in tokens:
            if x == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            
            elif x == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            
            elif x == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            
            elif x == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(int(left / right))
            
            else:
                stack.append(int(x))
            

        return stack.pop()