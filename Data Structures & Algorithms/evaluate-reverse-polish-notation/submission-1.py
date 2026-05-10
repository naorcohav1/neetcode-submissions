class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        dic = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }  
        value = 0
        for token in tokens:
            if token in ['+','-','*','/']:
                second = stack.pop()
                first = stack.pop()
                stack.append(dic[token](int(first),int(second)))
            else:
                stack.append(token)
        return int(stack[-1])
            