class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        
        bounces = 1
        
        while (bounces * q) % p != 0:
            bounces += 1
        
        if bounces % 2 == 0:
            return 2
        elif ((bounces * q) / p) % 2 == 0:
            return 0
        else:
            return 1