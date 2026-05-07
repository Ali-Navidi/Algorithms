class Solution:
    def groupAnagrams(self, strs):
        """
        Groups anagrams together using a brute force approach.

        Time Complexity: O(n^2 * m) where n is the number of strings and m is the average string length
        - Outer loop: O(n) iterations
        - For each string, we check against all remaining strings: O(n)
        - For each pair comparison, we count character frequencies: O(m)

        This approach is inefficient for large inputs but works by:
        1. Iterating through each string as a potential group starter
        2. For each starter, checking all subsequent strings for anagram relationship
        3. Using character count comparison to determine if strings are anagrams
        4. Collecting anagrams into groups and avoiding duplicates
        """
        actual_result = []
        for i in range(len(strs)):
            result = [strs[i]]  # Start a new group with current string
            already_grouped = False
            # Check if current string is already in an existing group
            for groups in actual_result:
                if result[0] in groups:
                    already_grouped = True
            if not already_grouped:
                # Look for anagrams of current string in remaining strings
                for j in range(i+1, len(strs)):
                    if len(strs[i]) != len(strs[j]):
                        continue  # Skip if lengths don't match (optimization)
                    is_anagram = True
                    # Check if character counts match for all unique characters
                    for char in set(strs[i]):
                        if strs[i].count(char) != strs[j].count(char):
                            is_anagram = False
                            break
                    if is_anagram:
                        result.append(strs[j])  # Add anagram to current group
                actual_result.append(result)  # Add completed group to results
        print(actual_result)
        return actual_result

    def groupAnagrams2(self, strs):
        """
        Groups anagrams together using a hashmap approach with sorted strings as keys.

        Time Complexity: O(n * m log m) where n is the number of strings and m is the average string length
        - Sorting each string: O(m log m) per string
        - Hashmap operations: O(1) average case for dictionary access

        This is the optimal approach that works by:
        1. Sorting each string to create a unique key for anagrams
        2. Using a dictionary to group strings with identical sorted versions
        3. Returning the dictionary values as the grouped anagrams
        """
        anagrams_dict = {}
        for word in strs:
            # Sort the word to create a unique key for all anagrams
            sorted_word = "".join(sorted(word))
            if sorted_word not in anagrams_dict:
                # Create new group for this anagram pattern
                anagrams_dict.update({sorted_word: [word]})
            else:
                # Add word to existing anagram group
                anagrams_dict[sorted_word].append(word)
        return list(anagrams_dict.values())
a = Solution()
a.groupAnagrams2(["eat","tea","tan","ate","nat","bat"])