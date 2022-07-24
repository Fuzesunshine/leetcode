class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
    
        def splitStr(input_str):
            list_str = list(input_str)
            cap_idx_list = []
            for idx, c in enumerate(list_str):
                if c.isupper():
                    cap_idx_list.append(idx)
            res = []
            cap_idx_list.append(len(list_str))
            for i in range(len(cap_idx_list) - 1):
                res.append(list_str[cap_idx_list[i]:cap_idx_list[i+1]])
            return res
        
        ans_list = []
        pattern_split_res = splitStr(pattern)
        for q_num, query in enumerate(queries):
            query_split_res = splitStr(query)
            if len(pattern_split_res) != len(query_split_res):
                ans_list.append(False)
                continue
            for p_sub, q_sub in zip(pattern_split_res, query_split_res):
                if len(p_sub) > len(q_sub):
                    ans_list.append(False)
                    break
                if p_sub[0] != q_sub[0]:
                    ans_list.append(False)
                    break
                    
                p_sub = p_sub[1:]
                q_sub = q_sub[1:]
                result = True
                for p in p_sub:
                    found = False
                    for idx, q in enumerate(q_sub):
                        if p == q:
                            found = True
                            q_sub = q_sub[idx+1:]
                            break
                    if found == False:
                        result = False
                        break
                        
                if result == False:
                    ans_list.append(result)
                    break
            if len(ans_list) - 1 < q_num:
                ans_list.append(True)
        return ans_list