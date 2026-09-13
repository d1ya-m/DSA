class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l=0
        r=len(nums)-1

        if(target<nums[l]): return 0
        if(target>nums[r]): return r+1

        while(l<=r):
            mid=l+(r-l)//2 #floor div
            if (nums[mid]==target):
                return mid
            elif (target<nums[mid]):
                r=mid-1
            else:
                l=mid+1
        return l
        