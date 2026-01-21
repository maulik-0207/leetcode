class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        haystack_len = len(haystack)
        needle_len = len(needle)
        if haystack_len < needle_len: return -1
        for i in range(0, haystack_len):
            if haystack[i] == needle[0]:
                for j in range(0, needle_len):
                    if (i+j) >= haystack_len: return -1
                    if haystack[i + j] != needle[j]:
                        break
                    if j == needle_len - 1:
                        return i
        return -1
                                            
        
if __name__ == '__main__':
    obj = Solution()
    pre= obj.strStr("sadbutsad", "sad")
    pre1= obj.strStr("leetcode", "leeto")
    pre1= obj.strStr("mississippi", "issipi")
    print(pre)
    print(pre1)
    