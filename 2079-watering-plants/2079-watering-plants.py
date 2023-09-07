class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        res = 0
        cur_capacity = capacity
        
        for k, plant in enumerate(plants):
            if cur_capacity >= plant:
                res += 1
                cur_capacity -= plant
            else:
                # refill can
                res += 2*k
                cur_capacity = capacity
                # water plant
                res += 1
                cur_capacity -= plant
        
        return res
    