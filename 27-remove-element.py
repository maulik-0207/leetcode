class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums: return 0
        j = -1
        for i in range(0, len(nums)):
            if nums[i] != val:
                j += 1
                nums[j] = nums[i]  

        return j + 1
            
if __name__ == '__main__':
    obj = Solution()
    list1 = [3,2,2,3]
    list2 = [0,1,2,2,3,0,4,2]
    pre= obj.removeElement(list1, 3)
    pre1= obj.removeElement(list2, 2)

    print(list1)
    print(pre)
    print(list2)
    print(pre1)
            