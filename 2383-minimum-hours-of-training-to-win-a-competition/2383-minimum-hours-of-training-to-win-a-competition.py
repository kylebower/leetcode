class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # define variables
        hours = 0
        n = len(energy)
        curExp = initialExperience
        curEner = initialEnergy
        
        # iterate to find number of training hours required to defeat all opponents
        for i in range(n):
            # need strictly greater experience and energy to defeat opponent i
            oppExp = experience[i]
            oppEner = energy[i]
            if oppExp >= curExp:
                trainingReq = oppExp - curExp + 1
                hours += trainingReq
                curExp += trainingReq
            if oppEner >= curEner:
                trainingReq = oppEner - curEner + 1
                hours += trainingReq
                curEner += trainingReq
            # Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i]
            curExp += oppExp
            curEner -= oppEner
        
        # Return the minimum number of training hours required to defeat all n opponents
        return hours
        
        # time complexity: O(n)
        # space complexity: O(1)
        