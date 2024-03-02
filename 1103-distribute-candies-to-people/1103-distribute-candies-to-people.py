class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        num_candies = [0]*num_people
        current = 1
        while candies > 0:
            candy_to_give = min(current, candies)
            num_candies[(current-1)%num_people] += candy_to_give
            candies -= candy_to_give
            current += 1
        return num_candies
    