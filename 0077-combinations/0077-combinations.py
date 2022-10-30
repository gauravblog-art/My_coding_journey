class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        
    
      nums=list(range(1,n+1))
      
      lst=[]
      def solver(nums,ans,k):
        
        if len(ans)==k:
          lst.append(ans)
          return 
      
        for i in range(len(nums)):
          
          solver(nums[i+1:], ans+[nums[i]],k)
      solver(nums,[],k)
      
      return lst