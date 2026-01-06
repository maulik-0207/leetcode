class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I": [None , 1],
            "V": ["I",5],
            "X": ["I",10],
            "L": ["X",50],
            "C": ["X",100],
            "D": ["C",500],
            "M": ["C", 1000],
        }
        ans = 0
        pre_roman = ""
        for roman in s:
            ans += (roman_dict[roman][1] - (roman_dict[roman_dict[roman][0]][1] if roman_dict[roman][0] == pre_roman else 0 ) - (roman_dict[roman_dict[roman][0]][1] if roman_dict[roman][0] == pre_roman else 0 ))
            pre_roman = roman
        return ans
        
if __name__ == '__main__':
    obj = Solution()
    ans = obj.romanToInt("III")
    print(ans)
    print("0".center(15, "-"))
    ans1 = obj.romanToInt("LVIII")
    print(ans1)
    print("0".center(15, "-"))
    ans2 = obj.romanToInt("MCMXCIV")
    print(ans2)
    print("0".center(15, "-"))