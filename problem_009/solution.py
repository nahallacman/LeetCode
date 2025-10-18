class Solution:
    def isPalindrome(self, x: int) -> bool:
        number_str = str(x)
        reverse_number_str = number_str[::-1]
        if(number_str == reverse_number_str):
            return True
        else:
            return False