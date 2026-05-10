class Solution:
    def isValid(self, s: str) -> bool:
        cur_stack = []
        for char in s:
            if char in ['{','[','(']:
                cur_stack.append(char)
            else:
                if cur_stack:
                    open = cur_stack.pop()
                else :
                    return False
                if (char == '}' and open != '{') or  (char == ']' and open != '[') or (char == ')' and open != '('):
                    return False
        return not cur_stack