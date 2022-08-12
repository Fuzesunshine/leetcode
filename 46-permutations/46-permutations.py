class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        
        def dfs(cur, rest):
            if len(rest) == 0:
                return res.append(cur)
            else:
                for idx in range(len(rest)):
                    dfs(cur+[rest[idx]], rest[0:idx]+rest[idx+1:])
        
        dfs([], nums)
        
        return res
