class Solution(object):
    def maxLength(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.res = 0
        visited = set()
        t = []
        for s in arr:
            if len(set(s)) == len(s):
                t.append(s)
        arr = t[:]

        def dfs(start, tmp):
            self.res = max(self.res, len(tmp))
            if start >= len(arr):
                return
            for i in range(start + 1, len(arr)):
                if not (set(tmp) & set(arr[i])):
                    dfs(i, tmp + arr[i])
        
        for i, s in enumerate(arr):
            dfs(i, s)
        
        return self.res
                
        