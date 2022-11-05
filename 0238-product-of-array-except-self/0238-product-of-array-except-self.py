class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      
      if len(nums)==0:
        
        return []
      
      n=len(nums)
      
      left=[1]*n
      right=[1]*n
      
      for i in range(1,n):
        
        left[i]=nums[i-1]*left[i-1]
        
      for i in range(n-2,-1,-1):
        right[i]=nums[i+1]*right[i+1]
        
      for i in range(n):
        
        nums[i]=left[i]*right[i]
      return nums
        