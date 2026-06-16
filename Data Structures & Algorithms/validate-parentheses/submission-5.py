class Solution:
    def isValid(self, s: str) -> bool:
        if not   s:
            return False
        stack=[]
        par_dict={')':'(',']':'[','}':'{'}
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            if i==')' or i=='}' or i==']':
                try:
                    if stack[-1] ==par_dict[i]:
                        stack.pop()
                    else:
                        return False
                except IndexError:
                    return False
        if not stack:
            return True
        else:
            return False
        