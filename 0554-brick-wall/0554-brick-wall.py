class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
      
      # here we find the total gap 
      greekGap={0:0}
      
      for r  in wall:
        
        total=0
        
        for i in r[:-1]:
          total+=i
          
          greekGap[total]=1+greekGap.get(total,0)
      
      # formula is that
      
      # gap = total row - total gap
      # print(greekGap)
      # print(max(greekGap.values()))
      return len(wall) - max(greekGap.values())
          
        