class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
      ans=0
      s=set(nums)
      for i in range(len(nums)):
        
        cur=nums[i]
        prv=cur-1
        c=0
        
        if prv not in s:
          
          while cur in s:
            c+=1
            cur+=1
        ans=max(ans,c)
        
        
      return ans
          
        
        
        
        
        