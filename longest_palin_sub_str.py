class Solution:
    non_palindromic_strs = set()
    
    def is_palindrome(self, s: str, len_s: int) -> bool:
        # print(s)
        start_ptr = 0
        end_ptr = len_s - 1
        while start_ptr < end_ptr:
            if s[start_ptr] != s[end_ptr]:
                return False
            start_ptr += 1
            end_ptr -= 1

        return True
    
    def get_longest_child_palindrome(self, ls: list[str], len_s: int):
        children = []
        for s in ls:
            children.extend([s[1:], s[:-1]])

            if s in self.non_palindromic_strs:
                continue
                
            if self.is_palindrome(s, len_s):
                return s
            else:
                self.non_palindromic_strs.add(s)

        return self.get_longest_child_palindrome(children, len_s-1)

    def longestPalindrome(self, s: str) -> str:
        len_s = len(s)
        # Condition where the input string is itself a palindrome
        if self.is_palindrome(s, len_s):
            return s
        longest_palindromic_str = self.get_longest_child_palindrome([s[1:], s[:-1]], len_s-1)
        return longest_palindromic_str
                    

s = Solution()

assert s.is_palindrome("abba", 4) == True
assert s.is_palindrome("bbabb",5) == True
assert s.is_palindrome("cad", 3) == False
assert s.is_palindrome("a", 1) == True
assert s.longestPalindrome("eabcb") == "bcb"
assert s.longestPalindrome("bb") == "bb"
assert s.longestPalindrome("cbbd") == "bb"
assert s.longestPalindrome("c") == "c"

# s.longestPalindrome("babaddtattarrattatddetartrateedredividerb")
