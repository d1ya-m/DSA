class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack=[]
        answers=[0]*len(temperatures)
        
        for i in range (len(temperatures)):
            while(stack and temperatures[stack[-1]]<temperatures[i]):
                prev=stack.pop()
                answers[prev]=i-prev
                
            stack.append(i)

            
        return answers 
            









        