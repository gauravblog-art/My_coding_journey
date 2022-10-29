class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        
        for i in range(len(nums)):
          n=target-nums[i]
          if  n in dic:
            return [dic[n],i]
          else:
            dic[nums[i]]=i
       