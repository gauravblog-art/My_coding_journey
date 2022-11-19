class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
      
      
      ans=0
      
      dic=dict()
      dic[0]=1
      
      total_sum=0
      for num in nums:
        
        total_sum=total_sum+num
        if total_sum-k in dic:
          ans+=dic[total_sum-k]
        if total_sum not in dic:
          dic[total_sum]=1
        else:
          
          dic[total_sum]+=1
      return ans
    
      