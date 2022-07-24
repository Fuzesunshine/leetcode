class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def splitVersion(version_str):
            res = []
            pre_zero = True
            split_str = ""
            for c in version_str:
                if c == ".":
                    res.append(split_str)
                    split_str = ""
                    pre_zero = True
                elif c=="0" and pre_zero:
                    continue
                else:
                    split_str += c
                    pre_zero = False
            res.append(split_str)
            return res
        
        split_list1 = splitVersion(version1)
        split_list2 = splitVersion(version2)
        
        if len(split_list1) > len(split_list2):
            split_list2 += ["" for _ in range(len(split_list1) - len(split_list2))]
        else:
            split_list1 += ["" for _ in range(len(split_list2) - len(split_list1))]
        
        print(split_list1)
        print(split_list2)
        
        for sub_version1, sub_version2 in zip(split_list1, split_list2):
            if len(sub_version1) > len(sub_version2):
                return 1
            elif len(sub_version1) < len(sub_version2):
                return -1
            else:
                for num1, num2 in zip(list(sub_version1), list(sub_version2)):
                    if int(num1) > int(num2):
                        return 1
                    elif int(num1) < int(num2):
                        return -1
        return 0
                    
                    
        