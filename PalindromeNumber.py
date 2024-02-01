class Solution:
    def isPalindrome(self, x: int) -> bool:
        palString = str(x)
        reversedString = ""

        for letter in palString:
            reversedString = letter + reversedString
        
        return palString == reversedString
