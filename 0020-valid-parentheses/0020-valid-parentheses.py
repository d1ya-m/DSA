class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for elem in s:
            if elem == '(' or elem == '[' or elem == '{':
                stack.append(elem)

            elif elem == ')' or elem == ']' or elem == '}':

                if len(stack) == 0:
                    return False

                if (elem == ')' and stack[-1] != '(' or
                    elem == ']' and stack[-1] != '[' or
                    elem == '}' and stack[-1] != '{'):
                    return False

                stack.pop()

        return len(stack) == 0