class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        # base case
        n = len(nums)
        number_good_pairs = 0
        if n < 2:
            return number_good_pairs
        
        # define dictionary to store count of each number
        new_dict = {}
        for i in range(n):
            new_dict.update({str(nums[i]):new_dict.get(str(nums[i]),0)+1})
        
        # iterate to find the number of good pairs
        for x in list(new_dict.keys()):
            count_x = new_dict.get(x)
            if count_x == 1:
                num_good_pairs_x = 0
            else:
                # Binomial coefficient: count_x C 2
                num_good_pairs_x = math.factorial(count_x) / math.factorial(count_x-2) / math.factorial(2)
            number_good_pairs += int(num_good_pairs_x)
        
        # return the number of good pairs
        return number_good_pairs
