class Solution(object):
    def countCollisions(self, directions):
        """
        :type directions: str
        :rtype: int
        """
        
        sum_l = 0
        sum_r = 0
        
        start = False
        
        for d in directions:
            if d == 'R':
                start = True
                sum_l += 1
            elif d == 'S':
                start = True
            elif d == 'L' and start:
                sum_l += 1
                
        for d in directions[::-1]:
            if d == 'R':
                sum_r += 1
            else:
                break
        
        return sum_l - sum_r
            
        
        