class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
      lst=[]
      def solver(nums,index,ans):
        
        if len(nums)<=index:
          lst.append(ans)
          return
        for i in range(index, len(nums)):
          temp=nums[i]
          nums[i]=nums[index]
          nums[index]=temp
          
          solver(nums,index+1,ans+[nums[index]])
          
          temp=nums[i]
          nums[i]=nums[index]
          nums[index]=temp
          
      solver(nums,0,[])
      
      return lst
        
        
        