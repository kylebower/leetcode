class Solution:
    def digitSum(self, s: str, k: int) -> str:
        # iterate to perform rounds
        while len(s) > k:        
            # Divide s into consecutive groups of size k
            divided_s = [s[k*i:k*(i+1)] for i in range(len(s)//k)] 
            if len(s)//k != len(s)/k:
                divided_s += [s[k*(len(s)//k):]]
            # Replace each group of s with a string representing the sum of all its digits
            for i, group in enumerate(divided_s):
                cur_sum = sum([int(c) for c in group])
                divided_s[i] = str(cur_sum)            
            # Merge consecutive groups together to form a new string
            s = ''.join(divided_s)
        
        # Return s after all rounds have been completed
        return s