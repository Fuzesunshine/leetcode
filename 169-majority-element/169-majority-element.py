class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt_dict = {}
        for num in nums:
            if num in cnt_dict:
                cnt_dict[num] += 1
            else:
                cnt_dict[num] = 1
            
            if cnt_dict[num] > len(nums) // 2:
                return num
