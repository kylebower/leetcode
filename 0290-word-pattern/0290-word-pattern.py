class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # make dict for pattern and s
        dp = {}
        ds = {}
        for i,p in enumerate(pattern):
            dp[p] = dp.get(p,[]) + [i]
        
        for i,word in enumerate(s.split()):
            ds[word] = ds.get(word,[]) + [i]
        
        return list(ds.values()) == list(dp.values())
    