class Solution(object):
    def removeDuplicates(self, nums: list[int]):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]  

        return j + 1
            
if __name__ == '__main__':
    obj = Solution()
    list1 = [1,1,2]
    list2 = [0,0,1,1,1,2,2,3,3,4]
    pre= obj.removeDuplicates(list1)
    pre1= obj.removeDuplicates(list2)

    print(list1)
    print(pre)
    print(list2)
    print(pre1)
            