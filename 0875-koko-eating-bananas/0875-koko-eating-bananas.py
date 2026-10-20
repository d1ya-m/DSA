class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        l=1
        r=max(piles)
        
        while(l<r):
            hours=0

            k=(l+r)//2

            for p in piles:

                hours+=(p+k-1)//k
            if hours<=h: 

                r=k
            else:
                l=k+1
        return l
