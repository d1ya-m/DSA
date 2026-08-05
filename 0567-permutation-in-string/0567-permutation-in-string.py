class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if(len(s1)>len(s2)):
            return False

        left=0
        right=len(s1)-1
        d={}
        for i in range (len(s1)):
            d[s1[i]]=d.get(s1[i], 0)+1

        d1={}
        for i in range(left, right+1):
            d1[s2[i]]=d1.get(s2[i], 0)+1

        while(right<len(s2) and left<=len(s2)-len(s1)):

        
 
            if (d1==d):
                return True
            d1[s2[left]]-=1
            if(d1[s2[left]]==0):
                del d1[s2[left]]
            left+=1
            right+=1
            if(right<len(s2)):
                d1[s2[right]]=d1.get(s2[right],0)+1
        return False


            
        
        