class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        
        lst=[]
        nums.sort()
        def solver(nums,ans):
          
          if len(nums)==0:
            lst.append(ans)
            return
            
          # ignore
          solver(nums[1:], ans)
          
          solver(nums[1:], ans + [nums[0]])
        solver(nums,[])
        
        lst1=[]
        for i in lst:
          lst1.append(tuple(i))
        s=set(lst1)
        lss=list(s)
        ls1=[]
        for i in lss:
          ls1.append(list(i))
        return ls1