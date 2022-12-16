class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        print(n)
        # Base case
        if n < 3:
            return []
        
        # sort array
        print(nums)
        nums.sort()
        print(nums)
        
        result = []
        for p0 in range(n-2):
            if p0 != 0 and nums[p0] == nums[p0-1]:
                continue
            # define pointers
            p1 = p0+1
            p2 = n-1
            while p1 < p2:
                current_sum = nums[p0] + nums[p1] + nums[p2]
                if current_sum == 0:
                    if nums[p1] == nums[p1+1] and p1+1 < p2:
                        p1 += 1                
                    elif nums[p2] == nums[p2-1] and p1 < p2-1:
                        p2 -= 1
                    else:
                        result.append([nums[p0],nums[p1],nums[p2]])
                        p1 += 1
                        p2 -= 1
                elif current_sum > 0:
                    p2 -= 1
                else:
                    p1 += 1
        return result
