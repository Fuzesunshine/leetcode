class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        
        l = len(s)
        
        if l % k != 0:
            fill_s = ''.join([fill for i in range(k - l % k)])
            s = s + fill_s
        res = []
        for idx in range(len(s) // k):
            res.append(s[idx*k:(idx+1)*k])
            
        return res
