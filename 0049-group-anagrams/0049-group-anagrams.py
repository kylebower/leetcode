class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # make array of dict for each word in strs
        array_dicts = []
        res = []
        for s in strs:
            ds = {}
            for c in s:
                ds[c] = ds.get(c,0)+1
            
            new_dic = 1
            for i in range(len(array_dicts)):
                if array_dicts[i] == ds:
                    new_dic = 0
                    x = res[i]
                    x.append(s)
                    res[i] = x
                    break
            if new_dic:
                array_dicts.append(ds)
                res.append([s])
        
        # return answer
        return res
