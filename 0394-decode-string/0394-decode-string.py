class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        num=0
        for i in s:
            if (i.isdigit()):
                num=num*10+int(i)
            elif (i=='['):
                stack.append(num)
                stack.append(i)
                num=0

            elif (i==']'):
                temp=[]
                while  stack[-1]!='[':
                    temp.append(stack.pop()) #another stack
                stack.pop() #remove open bracket
                
                count=stack.pop()
                decoded=''.join(reversed(temp))
                stack.append(count*decoded)
            else:
                stack.append(i)
        return ''.join(stack)

