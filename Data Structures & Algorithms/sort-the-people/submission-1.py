class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        # Created a hasmap
        height_to_name = {}
        
        # Zipped the values and looped through, mapping the height to the name
        for h, n in zip(heights, names):
            height_to_name[h] = n

        # Created an empty list
        res = []

        # Looped through a sorted list of heights, reversed it so it is in descending order.
        # Added the height to the list
        for h in reversed(sorted(heights)):
            res.append(height_to_name[h])

        # Returned the list
        return res