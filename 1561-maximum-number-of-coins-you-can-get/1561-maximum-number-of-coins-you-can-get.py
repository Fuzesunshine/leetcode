class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        
        sort_piles = sorted(piles, reverse=True)
        res = 0
        
        for i in range(len(sort_piles)//3):
            res += sort_piles[2*i+1]
            
        return res
    