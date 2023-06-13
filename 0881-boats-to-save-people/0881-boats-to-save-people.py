class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # sort people by weight
        people.sort()
        
        # count number of boats needed
        count = 0
        L = 0
        n = len(people)
        R = n-1
        while L<=R:
            if people[L] + people[R] > limit:
                R -= 1
                count += 1
            else:
                L += 1
                R -= 1
                count += 1
        
        # return number of boats
        return count
    