class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        
        cur_len = -1
        res = []
        pad_words = []
        
        for word in words:
            if cur_len + len(word) + 1 > maxWidth:
                if len(pad_words) == 1:
                    res.append(pad_words[0]+' '*(maxWidth-cur_len))
                else:
                    base_num = (maxWidth-cur_len)//(len(pad_words) - 1)
                    space_nums = [1+base_num] * (len(pad_words) - 1)
                    for i in range((maxWidth-cur_len)%(len(pad_words) - 1)):
                        space_nums[i] += 1
                                        
                    s = ''
                    for i in range(len(space_nums)):
                        s += (pad_words[i] + ' '*space_nums[i])
                    
                    s += pad_words[-1]
                    res.append(s)
                
                cur_len = -1
                pad_words = []
                    
            cur_len += len(word) + 1
            pad_words.append(word)
                    
        res_space_num = maxWidth - cur_len
        s = ''
        for i in range(len(pad_words)-1):
            s += (pad_words[i] + ' ')
            
        s += (pad_words[-1] + ' '*res_space_num)
        res.append(s)
        
        return res
        