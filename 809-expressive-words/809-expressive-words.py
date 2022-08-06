class Solution(object):
    def expressiveWords(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        def stat_string(input_str):
            cnt = [1]
            chars = [input_str[0]]

            for char in input_str[1:]:
                if char != chars[-1]:
                    chars.append(char)
                    cnt.append(1)
                else:
                    cnt[-1] += 1
            return cnt, chars
        
        res = 0
        
        s_cnt, s_chars = stat_string(s)

        for word in words:
            w_cnt, w_chars = stat_string(word)

            if len(w_chars) != len(s_chars):
                continue
            else:
                i = 0
                j = 0
                while i < len(w_chars) and j < len(s_chars):

                    if w_chars[i] == s_chars[j] and w_cnt[i] == s_cnt[j]:
                        i += 1
                        j += 1
                    elif w_chars[i] == s_chars[j] and w_cnt[i] < s_cnt[j] and s_cnt[j] > 2:
                        i += 1
                        j += 1
                    else:
                        j += 1
                if i == len(w_chars):
                    res+=1
                print(res)
                
        
        return res
                
                

        
        