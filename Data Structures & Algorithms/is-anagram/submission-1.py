class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): # Checks if the lengths aren't equal and returns False as if they aren't then they can't be anagrams
            return False

        countS, countT = {}, {} # initialise two empty hashmaps

        for i in range(len(s)): # Loops through the range of the first string
            countS[s[i]] = 1 + countS.get(s[i], 0) # Increments the count for both strings
            countT[t[i]] = 1 + countT.get(t[i], 0) # Increments the count for both strings
        for c in countS: # Checks if c is in the string, if it isn't, return False, else, continue until the string is complete
            if countS[c] != countT.get(c, 0):
                return False

        return True # Return True if both hashmaps match.
