class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        best_sum_so_far = sum(nums[:3])
        best_difference = abs(best_sum_so_far - target)
        
        # Base case
        if n == 3:
            return best_sum_so_far
        
        # iterate to find sum is closest to target
        for p0 in range(n-2):
            # define pointers
            p1 = p0 + 1
            p2 = n-1
            while p1 < p2:
                current_sum = nums[p0] + nums[p1] + nums[p2]
                current_difference = abs(current_sum - target)
                if current_difference < best_difference:
                    best_difference = current_difference
                    best_sum_so_far = current_sum
                if current_sum < target:
                    p1 += 1
                elif current_sum > target:
                    p2 -= 1
                else: # current_sum == target
                    return best_sum_so_far
        
        # return result
        return best_sum_so_far
    
    # Time complexity: O(n^2)
    # Space complexity: O(1)
