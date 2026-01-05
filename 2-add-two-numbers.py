# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        num1 = ""
        num2 = ""
        
        while l1.next:
            num1 += str(l1.val)
            l1 = l1.next
        num1 += str(l1.val)
        
        while l2.next:
            num2 += str(l2.val)
            l2 = l2.next
        num2 += str(l2.val)
        
        num3 = str(int(num1[::-1]) + int(num2[::-1]))
        
        next_node = None
        
        for num in num3:
                
            next_node = ListNode(val= int(num), next=next_node)
        
        return next_node
    
if __name__ == '__main__':
    next_node_1 = None
    for i in [3,4,2]:
        next_node_1 = ListNode(val= i, next= next_node_1)
    next_node_2 = None
    for i in [4,6,5]:
        next_node_2 = ListNode(val= i, next= next_node_2)
        
    obj = Solution()
    node = obj.addTwoNumbers(next_node_1, next_node_2)
    while node.next:
            print(node.val)
            node = node.next
    print(node.val)