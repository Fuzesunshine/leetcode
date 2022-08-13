class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        m = len(words[0])
        n = len(words)
        l = len(s)
        res = []
        
        for start_idx in range(m):
            remain_words = []+words
            visited_words = []
            for i in range((l-start_idx)//m):
                piece = s[i*m+start_idx:(i+1)*m+start_idx]
                if len(visited_words) == n:
                    remain_words.append(visited_words.pop(0))
                
                if piece in remain_words:
                    remain_words.remove(piece)                        
                    visited_words.append(piece)
                    if len(remain_words) == 0:
                        res.append((i+1-n)*m+start_idx)
                elif piece in visited_words:
                    last_idx = visited_words.index(piece)
                    for j in range(last_idx):
                        remain_words.append(visited_words.pop(0))
                    visited_words.pop(0)
                    visited_words.append(piece)
                else:
                    remain_words = []+words
                    visited_words = []

        return res 
        