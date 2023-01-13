import numpy as np
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        # define direction and normal vectors for line
        direction_vector = [coordinates[1][1]-coordinates[0][1], coordinates[1][0]-coordinates[0][0]]
        normal_vector = [direction_vector[1], -direction_vector[0]]
        
        # iterate to check if these points make a straight line in the XY plane
        for i in range(2,len(coordinates)):
            direction_vector_i = [coordinates[i][1]-coordinates[0][1],coordinates[i][0]-coordinates[0][0]]
            # return false if new direction vector is not orthogonal to normal vector
            if np.dot(direction_vector_i, normal_vector) !=0:
                return False
        
        # return true if coordinates make a straight line in the XY plane
        return True
