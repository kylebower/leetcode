class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        print(num)
        while num != 0:
            print(num)
            if num % 2 == 0:
                num = num/2
            else:
                num = num - 1
            result += 1
        return result
            
        