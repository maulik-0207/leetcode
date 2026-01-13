class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp = abs(x)
        new = 0
        while temp != 0:
            new = (new*10) + temp % 10
            temp = temp // 10

        if x + abs(x) == 0:
            if (new * -1) < -2**31:
                return 0
            return (new * -1)
        else:
            if new >  2**31 - 1:
                return 0
            return new
    
if __name__ == '__main__':
    obj = Solution()
    num1 = obj.reverse(123)
    num2 = obj.reverse(-123)
    num3 = obj.reverse(120)
    num4 = obj.reverse(1534236469)
    num4 = obj.reverse(-2147483648)
    print(num1)
    print(num2)
    print(num3)
    print(num4)