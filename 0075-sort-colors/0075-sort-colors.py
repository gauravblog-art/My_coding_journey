class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a=nums.count(1)
        b=nums.count(0)
        c=nums.count(2)
        
        
  
        for i in range(b):
        
          nums[i]=0
        for i in range(b,a+b):
         
          nums[i]=1
        for i in range(a+b,a+b+c):
          nums[i]=2
        
        