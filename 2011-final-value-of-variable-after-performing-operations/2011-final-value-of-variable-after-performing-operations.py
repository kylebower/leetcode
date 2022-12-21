class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # define number X
        X = 0
        
        # iterate to increment and decrement X
        for i in range(len(operations)):
            increment_i = operations[i] == "X++" or operations[i] == "++X"
            if increment_i:
                X += 1
            else:
                X -= 1
            
        # return final value of X
        return X
