class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      
      ans=0
      n=len(nums)
      s=set(nums)
      
      for i in range(n):
        curr=nums[i]
        prev=curr-1
        c=0
        if prev not in s:
          
          while curr in s:
            c+=1
            curr+=1
        ans=max(c,ans)
      return ans
          
        
        
        
        
        