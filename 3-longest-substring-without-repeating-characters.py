class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = {}         # char -> last index seen
        start = 0         # left boundary of current window
        max_len = 0

        for i, ch in enumerate(s):
            prev = last.get(ch, -1)
            if prev >= start:
                # character repeated inside current window -> move start
                start = prev + 1
            last[ch] = i
            # update max length
            if i - start + 1 > max_len:
                max_len = i - start + 1

        return max_len
            
        
        
if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLongestSubstring('pwwkew'))