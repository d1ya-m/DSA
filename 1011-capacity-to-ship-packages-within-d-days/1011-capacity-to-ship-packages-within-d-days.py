class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:

        l=max(weights)
        r=sum(weights)

        while l<r:

            d=1 #start at d=1 cause u do d+=1 only when cap is exceeded
            cap=(l+r)//2
            load=0

            for w in weights:

                if load+w>cap:
                    d+=1
                    load=w
                else:
                    load+=w

            if d<=days:
                r=cap
            else:
                l=cap+1
        return l
        