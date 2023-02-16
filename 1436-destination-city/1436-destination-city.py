class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        # make dict where key-value pair represents direct path from key to value city
        d = {}
        for p in paths:
            d[p[0]] = p[1]
            
        # iterate until we arrive at destination
        current_location = paths[0][0]
        while current_location in d:
            current_location = d[current_location]
        
        # return destination city
        return current_location
    