class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
      
      
      lst=[]
      def solver(candidates,target,ans):
        
        if target<0:
          return
        
        if target==0:
          lst.append(ans)
          return
        
        for i in range(len(candidates)):
          
          solver(candidates[i:], target-candidates[i], ans+[candidates[i]])
          
          
          
      solver(candidates,target,[])
      return lst
              
            