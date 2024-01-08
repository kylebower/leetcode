class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res = []
        
        d = {}
        for cpd in cpdomains:
            rep, domain = cpd.split(" ")
            domains = domain.split(".")
            for i,_ in enumerate(domains):
                d[".".join(domains[i:])] = d.get(".".join(domains[i:]),0) + int(rep)
        
        for key in d:
            res.append(str(d[key]) + " " + key)
        
        return res
    