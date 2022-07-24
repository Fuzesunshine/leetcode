class Solution(object):
    def countRangeSum(self, nums, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: int
        """
        
        s_list = [0]
        s_cur = 0
        ans = 0
        for num in nums:
            s_cur += num
            ans += (bisect.bisect_right(s_list, s_cur - lower) - bisect.bisect_left(s_list, s_cur-upper))
            bisect.insort(s_list, s_cur)
        
        return ans
    