class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

      lst=[]
      candidates.sort()
      def solver(candidates, target, ans):
        
        if target<0:
          return
        
        if target==0:
          lst.append(ans)
          return
        
        for i in range(len(candidates)):
          
          if i>=1 and candidates[i]==candidates[i-1]:
            continue
          
          solver(candidates[i+1:], target-candidates[i], ans+[candidates[i]])
      solver(candidates, target, [])
      
      return lst