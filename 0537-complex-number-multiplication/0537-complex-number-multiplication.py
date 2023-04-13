class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        n1_str = num1[:-1].split('+')
        n2_str = num2[:-1].split('+')
        a = int(n1_str[0])
        b = int(n1_str[1])
        c = int(n2_str[0])
        d = int(n2_str[1])
        return "%d+%di" % (a*c-b*d, b*c+a*d)
        