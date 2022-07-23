class Solution:
    def minInsertions(self, s: str) -> int:
        length = len(s)
        dp = [[0] * length for _ in range(length)] 
        
        for l in range(1, length):
            i = 0
            for j in range(l, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
                i += 1
        
        return dp[0][length-1]           

    # def minInsertions(self, s: str) -> int:
    #     @lru_cache(None)
    #     def dfs(l, r):
    #         if l >= r:
    #             return 0
    #         if s[l] == s[r]:
    #             return dfs(l+1, r-1)
    #         return 1 + min(dfs(l+1, r), dfs(l, r-1))
    #     return dfs(0, len(s)-1)
