class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left=0
        max_freq=0
        d={}

        max_win=1

        for right in range(len(s)):
            d[s[right]]=d.get(s[right],0)+1
            max_freq=max(max_freq, max(d.values()))
            
            while(right-left+1-max_freq>k):
                
                d[s[left]]-=1
                if(d[s[left]]==0):
                    del d[s[left]]
                left+=1
            max_win=max(max_win, right-left+1)
            
            
           

        return max_win

                
            

        