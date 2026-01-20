class Solution(object):
    
    stack = []
    index = -1
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        self.stack = []
        self.index = -1
        closing_brackets = {
            "}": "{", 
            "]": "[", 
            ")": "("
        }
        for bracket in s:
            if bracket in closing_brackets:
                if closing_brackets[bracket] != self.peek(): 
                    return False
                else:
                    self.pop()
            else:
               self.push(bracket)
        
        if self.index != -1:
            return False
        
        return True
        
    def push(self, x):
        self.index += 1
        self.stack.append(x)
        
    def pop(self):
        if self.index == -1:
            return False
        
        self.index -= 1
        return self.stack.pop()
    
    def peek(self):
        if self.index == -1:
            return False
        
        return self.stack[self.index]
        
if __name__ == '__main__':
    obj = Solution()
    pre= obj.isValid("()")
    pre1= obj.isValid("()[]{}")
    pre2= obj.isValid("(]")
    pre3= obj.isValid("([])")
    pre4= obj.isValid("([)]")
    pre5= obj.isValid("]")
    pre6= obj.isValid("[")
    print(pre)
    print(pre1)
    print(pre2)
    print(pre3)
    print(pre4)
    print(pre5)
    print(pre6)