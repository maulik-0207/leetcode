class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        end = len(strs[0])

        for string in strs:
            if len(string) < end: end = len(string)
            for i in range(0, end):
                if strs[0][i] != string[i]:
                    end = i
                    break
        
        return strs[0][:end]



if __name__ == '__main__':
    obj = Solution()
    pre= obj.longestCommonPrefix(["a"])
    pre1= obj.longestCommonPrefix(["flower", "flow", "fly"])
    pre2= obj.longestCommonPrefix(["ab", "a"])
    print(pre)
    print(pre1)
    print(pre2)