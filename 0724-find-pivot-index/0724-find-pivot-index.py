class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
      
      total_sum=sum(nums)
      num_arry=[]
      
      c=0
      
      for i in range(len(nums)):
        
        c+=nums[i]
        num_arry.append(c)
      
      for j in range(len(nums)):
        
        left=num_arry[j]-nums[j]
        right=total_sum-num_arry[j]
        
        if left==right:
          
          return j
      return -1
        