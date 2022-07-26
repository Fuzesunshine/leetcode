class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        return n > 0 and 3**20 % n ==0
        