class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1_str = num1.split('+')
        n2_str = num2.split('+')
        a = int(n1_str[0])
        b = int(n1_str[1][:len(n1_str[1])-1])
        c = int(n2_str[0])
        d = int(n2_str[1][:len(n2_str[1])-1])
        result = str(int(a*c-b*d)) + "+" + str(int(b*c+a*d)) + "i"
        return result
        