class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        num_candies = [0]*num_people
        current = 1
        count = 0
        while candies > 0:
            num_candies[count%num_people] += min(current, candies)
            candies -= min(current, candies)
            count += 1
            current += 1
        return num_candies
    