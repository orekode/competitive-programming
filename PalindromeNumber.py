class Solution:
    def isPalindrome(self, x: int) -> bool:
        palString = str(x)
        reversedString = palString[::-1]
        
        return palString == reversedString
