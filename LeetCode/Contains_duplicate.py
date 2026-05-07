class Solution:
    """
    Contains Duplicate (LeetCode)

    Goal:
    Given a list of integers, return True if any value appears at least twice.
    Return False if all elements are unique.

    Approach:
    - Use a set to keep track of values we have already seen.
    - Iterate through the list once.
    - For each number:
        - If it is already in the set, return True (duplicate found).
        - Otherwise, add it to the set.

    Time Complexity:
    - O(n)
    - We go through the list once, and search in a set is O(1)

    Space Complexity:
    - O(n)
    - In the worst case, we store all elements in the set
    """

    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()  # stores values we have already seen

        for num in nums:
            # check if the number is already seen
            if num in seen:
                return True

            # otherwise, add it to the set
            seen.add(num)

        return False
    """
    Approach 2:
    Use the property of a set: it does not store duplicate values.

    Idea:
    - Convert the list to a set
    - If duplicates exist, the size of the set will be smaller than the list

    Time Complexity:
    - O(n)

    Space Complexity:
    - O(n)
    """

    def containsDuplicate2(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
