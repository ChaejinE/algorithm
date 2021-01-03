class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        i = 0
        while i < len(strs):
            if strs.pop() != strs.pop(0):
                return False
            i += 1
        
        return True
        
