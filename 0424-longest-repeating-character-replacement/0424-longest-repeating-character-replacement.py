class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # base case
        n = len(s)
        if n < k:
            return n
        
        # define longest substring variable
        max_length = 0
        
        # define dictionary of all characters in s
        new_dict = {}
        for i in range(n):
            new_dict.update({s[i]:s[i]})
        
        # iterate to find longest substring
        for j in list(new_dict.values()):
            
            # define pointers for sliding window
            L = 0
            R = 0
            counter = 0
            while R < n:
                print(R)
                print(L)
                if s[R] != j:
                    counter += 1
                while counter > k:
                    if s[L] != j:
                        counter -= 1
                    L += 1
                max_length = max(max_length, R - L + 1)
                R += 1           
        
        # return longest substring
        return max_length
