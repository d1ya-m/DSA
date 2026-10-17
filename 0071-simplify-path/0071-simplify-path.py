class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        L = path.split('/')
        i = 0

        while i < len(L):
            if L[i] == '' or L[i] == '.':
                pass

            elif L[i] == '..':
                if stack:
                    stack.pop()

            else:
                stack.append(L[i])

            i += 1

        s = '/' + '/'.join(stack)
        return s