class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        summ=0

        for i in range(len(operations)):
            if (operations[i] not in ['C', '+', 'D']):
                s.append(int(operations[i]))
                summ+=int(operations[i])
            elif(operations[i]=='+'):
                a=s.pop()
                b=s.pop()
                s.append(b)
                s.append(a)
                s.append(a+b)
                summ+=s[-1]
            elif(operations[i]=='D'):
                s.append(s[-1]*2)
                summ+=s[-1]
            elif(operations[i]=='C'):
                summ-=s[-1]
                s.pop()
        return summ


            
        