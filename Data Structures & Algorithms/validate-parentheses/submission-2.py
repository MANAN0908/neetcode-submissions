class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {")": "(","]": "[","}": "{"}
        for char in s:
            if char in "[{(":
                stack.append(char)
            if char in "}])":
                if not stack:
                    return False
                if stack[-1]!=pairs[char]:
                    return False
                else:
                    stack.pop()
        return len(stack)==0


        