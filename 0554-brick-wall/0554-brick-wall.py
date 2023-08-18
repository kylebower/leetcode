class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        # make dict counting locations of breaks between bricks
        d = {}
        for row in wall:
            location = 0
            for brick in row[:-1]:
                location += brick
                d[location] = d.get(location,0) + 1
        
        # return minimum number of crossed bricks after drawing such a vertical line
        return len(wall) - max(list(d.values()) + [0])
    