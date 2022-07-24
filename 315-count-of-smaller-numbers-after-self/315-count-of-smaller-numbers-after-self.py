class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def binarySearch(sort_list, val):
            l = 0
            r = len(sort_list) - 1
            while l < r:
                mid = (l+r) // 2
                if sort_list[mid] < val:
                    l = mid + 1
                else:
                    r = mid
            return l
        
        sort_nums = sorted(nums)
        ans = []
        for num in nums:
            pos = binarySearch(sort_nums, num)
            sort_nums.pop(pos)
            ans.append(pos)
        
        return ans