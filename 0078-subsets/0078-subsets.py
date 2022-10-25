class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
      
      lst=[]
      
      def solver(nums,ans):
        
        if len(nums)==0:
          lst.append(ans)
          return 
        
        solver(nums[1:], ans)
        solver(nums[1:], ans+[nums[0]])
      
      solver(nums,[])
      
      return lst
        