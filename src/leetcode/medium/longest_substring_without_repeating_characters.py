"""
This right of the bat looks like a 2 pointer problem.
We have 1 pointer at the start, another at the start as well.
A variable for longest substring which could be a list (performance later. Set possible - but not sure if length
attribute would be available to us). If not, have another variable tracking the longest length.
Then we just move pointer 2 forward until we found a duplicate character.
Once / if we find a duplicate character, we can then move pointer 1 forward until we remove that duplicate character.
Once we do, we continue to iterate pointer 2 until the end of the string.
For every iteration, we are also updating the longest substring found so far and the longest substring itself.

---

Update, use a hashmap / dict to track the letter and the index of that letter to ensure first pointer immediately
goes to the right place.
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pass
