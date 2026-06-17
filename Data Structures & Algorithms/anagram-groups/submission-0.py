class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_ana={}
        strs_len=len(strs)
        ans_list=[]
        if not strs:
            return [""]
        temp_list=[]
        for i in range(0,strs_len):
            for j in range(0,strs_len):
                if "".join(sorted(strs[i]))=="".join(sorted(strs[j])):
                    temp_list.append(strs[j])
            dict_ana["".join(sorted(strs[i]))]=temp_list
            temp_list=[]
        for value in dict_ana.values():
            ans_list.append(value)
        return ans_list