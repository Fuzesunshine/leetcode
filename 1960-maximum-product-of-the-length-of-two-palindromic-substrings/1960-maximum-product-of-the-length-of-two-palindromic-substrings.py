class Solution(object):
    def maxProduct(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manacher(s):
            maxCenter = 0
            maxRight = 0
            n = len(s)
            radius = [0] * n
            
            for i in range(1, n):
                if maxRight > i:
                    minR = min(radius[2*maxCenter-i], maxRight-i)
                else:
                    minR = 0
                j = 1
                while (i-minR >=0) and (i+minR < n) and(s[i-minR]==s[i+minR]):
                    minR += 1
                radius[i] = minR - 1
                
                if i+radius[i] > maxRight:
                    maxRight = i+radius[i]
                    maxCenter = i
            
            return radius
        
        radius = manacher(s)        
        maxLeft = [0 for _ in range(len(s)-1)]
        maxRight = [0 for _ in range(len(s)-1)]
        
        j = 0
        for i in range(1, len(s)-1):
            addR = 0
            while(j < i):
                if radius[j] + j < i:
                    j += 1
                else:
                    addR = i-j
                    break
            maxLeft[i] = max(maxLeft[i-1], addR)
        
        j = len(s)-1
        for i in range(len(s)-3, -1, -1):
            addR = 0
            while(i + 1 < j):
                if j - radius[j] > i + 1:
                    j -= 1
                else:
                    addR = j - i - 1
                    break
            maxRight[i] = max(maxRight[i+1], addR)
        
        res = 0
        for maxL, maxR in zip(maxLeft, maxRight):
            if res < (2*maxL+1)*(2*maxR+1):
                res = (2*maxL+1)*(2*maxR+1)
        
        return res
        