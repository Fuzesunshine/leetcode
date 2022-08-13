class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        cnt_dict = {}
        res = []
        n = len(nums)
        
        for num in nums:
            
            if res:
                if num == res[0]:
                    continue
            
            if num in cnt_dict:
                cnt_dict[num] += 1
            else:
                cnt_dict[num] = 1
                
            if cnt_dict[num] > n//3:
                res.append(num)
                if len(res) > 1:
                    break
        
        return res
        