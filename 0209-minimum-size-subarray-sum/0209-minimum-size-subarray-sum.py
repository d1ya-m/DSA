class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minl=len(nums)+1
        
        right=0
        summ=nums[0]
    
        for left in range(len(nums)):
            
            
            while(summ<target and right<len(nums)-1):
                right+=1
                summ+=nums[right]
            if (summ<target):
                pass
            else:
                minl=min(minl, right-left+1)
            summ-=nums[left]

        if(minl>len(nums)):
            return 0
                
        return minl
            


      
        