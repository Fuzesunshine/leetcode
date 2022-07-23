class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m = len(str1)
        n = len(str2)
        dp = [["" for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if str1[i-1] == str2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + str1[i-1]
                else:
                    if len(dp[i-1][j]) > len(dp[i][j-1]):
                        dp[i][j] = dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-1]
                    
        str3 = dp[m][n]
        res = []
        list1 = list(str1)
        list2 = list(str2)
        for c in list(str3):
            i = list1.index(c)
            j = list2.index(c)
            res += list1[:i]
            res += list2[:j]
            res.append(c)
            del list1[:i+1]
            del list2[:j+1]
        
        res += (list1 + list2)
        
        return "".join(res)