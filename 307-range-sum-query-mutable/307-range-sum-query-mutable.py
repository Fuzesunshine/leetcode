class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_val = 0
        for num in nums:
            self.sum_val += num 
        self.l = len(nums)

    def update(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        self.sum_val = self.sum_val - self.nums[index] + val
        self.nums[index] = val
        

    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if right - left < self.l // 2:
            return sum(self.nums[left:right+1])
        else:
            return self.sum_val - sum(self.nums[:left]) - sum(self.nums[right+1:self.l])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)