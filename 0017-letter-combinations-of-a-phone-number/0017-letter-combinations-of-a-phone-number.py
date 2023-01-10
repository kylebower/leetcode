class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # define dictionary of letters corresponding to each digit
        letter_dict = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        
        # define output list
        result = []
        
        # append possible letter combinations to output list
        for d in digits:
            result = getLetterCombs(d,result,letter_dict)
        
        #  return all possible letter combinations
        return result

# function to add letter combinations corresponding to digit d
def getLetterCombs(d,result,letter_dict):
    old_result = result
    result = []
    if old_result == []:
        for ch in letter_dict[d]:
            result.append(ch)
    else:
        for r in old_result:
            for ch in letter_dict[d]:
                result.append(r+ch)
    return result