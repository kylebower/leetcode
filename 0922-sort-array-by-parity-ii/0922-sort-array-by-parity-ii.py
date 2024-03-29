class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # define two pointers
        L = 0
        R = 1
        
        # sort array using two pointers
        while R < len(nums):
            # find number out of place
            if nums[L]%2 == L%2:
                L += 1
                R += 1            
            # find number to swap
            elif nums[R]%2 != L%2:
                R += 1
            # swap two numbers
            else:
                temp = nums[R]
                nums[R] = nums[L]
                nums[L] = temp
                # increment pointers
                L += 1
                R = L + 1
        
        # return sorted array
        return nums
    