def remove_non_alphanumeric(s: str) -> str:
    return ''.join(char for char in s if char.isalnum())

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = remove_non_alphanumeric(s).lower()
        return s == s[::-1]