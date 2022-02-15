from typing import List, Tuple


class Solution:
    non_palindromic_strs: set = set()
    test: str = ""
    children: set = set()

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
        self, ptrs: List[Tuple[int, int]]
    ):
        children_ptrs = []

        # print("Ptrs to check")
        # print(ptrs)

        for left_ptr, right_ptr in ptrs:
            left_case = (left_ptr + 1, right_ptr)
            right_case = (left_ptr, right_ptr - 1)

            # print(left_case)
            # print(right_case)
            # print(self.children)
            
            if left_case not in self.children:
                children_ptrs.append(left_case)
                self.children.add(left_case)
            
            if right_case not in self.children:
                children_ptrs.append(right_case)
                self.children.add(right_case)

            str_to_check = self.test[left_ptr : right_ptr + 1]
            if str_to_check in self.non_palindromic_strs:
                continue

            if self.is_palindrome(str_to_check, (right_ptr - left_ptr) + 1):
                return str_to_check
            else:
                self.non_palindromic_strs.add(str_to_check)

        return self.get_longest_child_palindrome(children_ptrs)

    def longestPalindrome(self, s: str) -> str:
        self.children = set()
        self.non_palindromic_strs = set()
        self.test = ""
        # print(s)
        len_s = len(s)
        # Condition where the input string is itself a palindrome
        if self.is_palindrome(s, len_s):
            return s
        self.test = s
        longest_palindromic_str = self.get_longest_child_palindrome(
            [(0, len_s - 2), (1, len_s - 1)]
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

assert s.longestPalindrome("babaddtattarrattatddetartrateedredividerb") == "ddtattarrattatdd"

s.longestPalindrome("cyyoacmjwjubfkzrrbvquqkwhsxvmytmjvbborrtoiyotobzjmohpadfrvmxuagbdczsjuekjrmcwyaovpiogspbslcppxojgbfxhtsxmecgqjfuvahzpgprscjwwutwoiksegfreortttdotgxbfkisyakejihfjnrdngkwjxeituomuhmeiesctywhryqtjimwjadhhymydlsmcpycfdzrjhstxddvoqprrjufvihjcsoseltpyuaywgiocfodtylluuikkqkbrdxgjhrqiselmwnpdzdmpsvbfimnoulayqgdiavdgeiilayrafxlgxxtoqskmtixhbyjikfmsmxwribfzeffccczwdwukubopsoxliagenzwkbiveiajfirzvngverrbcwqmryvckvhpiioccmaqoxgmbwenyeyhzhliusupmrgmrcvwmdnniipvztmtklihobbekkgeopgwipihadswbqhzyxqsdgekazdtnamwzbitwfwezhhqznipalmomanbyezapgpxtjhudlcsfqondoiojkqadacnhcgwkhaxmttfebqelkjfigglxjfqegxpcawhpihrxydprdgavxjygfhgpcylpvsfcizkfbqzdnmxdgsjcekvrhesykldgptbeasktkasyuevtxrcrxmiylrlclocldmiwhuizhuaiophykxskufgjbmcmzpogpmyerzovzhqusxzrjcwgsdpcienkizutedcwrmowwolekockvyukyvmeidhjvbkoortjbemevrsquwnjoaikhbkycvvcscyamffbjyvkqkyeavtlkxyrrnsmqohyyqxzgtjdavgwpsgpjhqzttukynonbnnkuqfxgaatpilrrxhcqhfyyextrvqzktcrtrsbimuokxqtsbfkrgoiznhiysfhzspkpvrhtewthpbafmzgchqpgfsuiddjkhnwchpleibavgmuivfiorpteflholmnxdwewj")