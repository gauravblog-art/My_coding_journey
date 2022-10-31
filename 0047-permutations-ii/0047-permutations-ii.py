class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
      
      
      lst=[]
      
      def solver(nums,ans, index):
        
        if len(nums)==index:
          lst.append(ans)
          
          return
        
        for i in range(index,len(nums)):
          
          temp=nums[index]
          nums[index]=nums[i]
          nums[i]=temp
          
          solver(nums,  ans+[nums[index]], index+1)
          
          temp=nums[index]
          nums[index]=nums[i]
          nums[i]=temp
      solver(nums,[], 0)
      
      return[ list(ls) for ls in set([tuple(l) for l in lst])]
        