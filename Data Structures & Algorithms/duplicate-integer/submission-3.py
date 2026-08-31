class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for n in nums: # Looping through the array
            if n in seen: # Check if n is in the hashset
                return True # If so, return True
            else: # Else, add to the set and continue.
                seen.add(n)
        return False # Return False if there are no duplicates