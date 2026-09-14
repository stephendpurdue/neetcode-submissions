class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.alphaNum(s[l]):
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True

    # This is a helper function which gets the ASCII values of the alphabet and numbers.
    def alphaNum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z") or 
            ord("a") <= ord(c) <= ord("z") or 
            ord("0") <= ord(c) <= ord("9"))


# Check if it reads the same from left to right and vice versa.
# Use two pointers to start from both ends
