class Solution:
    def checking(self , s:str):
        if ")" in s:
            return "("
        if "}" in s:
            return "{"
        else:
            return "["

    def isValid(self, s:str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            else:
                if len(stack) != 0 and stack[-1] == self.checking(i):
                    stack.pop()
                else:
                    return False
            

        return not stack