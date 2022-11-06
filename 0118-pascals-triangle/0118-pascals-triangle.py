class Solution(object):
    def generate(self, n):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal=[[1]*(i+1) for i in range(n)]
        
        for i in range(n):
          
          for j in range(1,i):
            
            pascal[i][j]=pascal[i-1][j-1]+pascal[i-1][j]
        return pascal