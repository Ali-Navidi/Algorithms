class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Initial check: If lengths differ, or the number of unique characters 
        # differ, they cannot be anagrams.
        if len(set(s)) != len(set(t)) or len(s) != len(t):
            return False
            
        # Iterate through each unique character found in string 's'
        for char in set(s):
            # PERFORMANCE Note: This is where the O(n^2) complexity comes from.
            # s.count(char) and t.count(char) each perform a full scan of the strings.
            # Since we do this inside a loop that iterates up to 'n' times,
            # the total time complexity becomes O(n * n) = O(n^2).
            if s.count(char) != t.count(char):
                return False
        
        # If all character counts match, it's a valid anagram
        return True