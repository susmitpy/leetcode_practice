from typing import List, Tuple


class Solution:
    non_palindromic_strs = set()

    def is_palindrome(self, s: str, len_s: int) -> bool:
        # print("Checking if palindrome")
        # print(s)
        # print(len_s)
        start_ptr = 0
        end_ptr = len_s - 1
        while start_ptr < end_ptr:
            if s[start_ptr] != s[end_ptr]:
                return False
            start_ptr += 1
            end_ptr -= 1

        return True

    def get_longest_child_palindrome(
        self, s: str, ptrs: List[Tuple[int, int]]
    ):
        children_ptrs = []

        # print("Ptrs to check")
        # print(ptrs)

        for left_ptr, right_ptr in ptrs:
            children_ptrs.extend([(left_ptr + 1, right_ptr), (left_ptr, right_ptr - 1)])

            str_to_check = s[left_ptr : right_ptr + 1]
            if str_to_check in self.non_palindromic_strs:
                continue

            if self.is_palindrome(str_to_check, (right_ptr - left_ptr) + 1):
                return str_to_check
            else:
                self.non_palindromic_strs.add(str_to_check)

        return self.get_longest_child_palindrome(s, children_ptrs)

    def longestPalindrome(self, s: str) -> str:
        # print(s)
        len_s = len(s)
        # Condition where the input string is itself a palindrome
        if self.is_palindrome(s, len_s):
            return s
        longest_palindromic_str = self.get_longest_child_palindrome(
            s, [(0, len_s - 2), (1, len_s - 1)]
        )
        return longest_palindromic_str


s = Solution()

assert s.is_palindrome("abba", 4) == True
assert s.is_palindrome("bbabb", 5) == True
assert s.is_palindrome("cad", 3) == False
assert s.is_palindrome("a", 1) == True
assert s.longestPalindrome("eabcb") == "bcb"
assert s.longestPalindrome("bb") == "bb"
assert s.longestPalindrome("cbbd") == "bb"
assert s.longestPalindrome("c") == "c"

s.longestPalindrome("babaddtattarrattatddetartrateedredividerb")
