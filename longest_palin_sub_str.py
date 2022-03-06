from typing import List, Set, Tuple, NewType

START_IDX = NewType("START_IDX", int)
END_IDX = NewType("END_IDX", int)


class Solution:
    input_str: str
    non_palin_idxs: Set[Tuple[START_IDX, END_IDX]]

    def is_palindrome(self, s: str, len_s: int) -> bool:
        start_idx = 0
        end_idx = len_s - 1

        while start_idx <= end_idx and s[start_idx] == s[end_idx]:
            start_idx += 1
            end_idx -= 1

        return start_idx > end_idx

    def get_longest_palin_among_children(
        self, children_ptrs: List[Tuple[START_IDX, END_IDX]]
    ) -> str:
        grand_children_ptrs: List[Tuple[START_IDX, END_IDX]] = []

        for start_idx, end_idx in children_ptrs:
            if start_idx == end_idx:
                return self.input_str[start_idx]

            str_to_check = self.input_str[start_idx : end_idx + 1]
            is_already_checked_non_palin = (start_idx, end_idx) in self.non_palin_idxs
            if not is_already_checked_non_palin and self.is_palindrome(
                str_to_check, (end_idx - start_idx) + 1
            ):
                # It is the longest palindrome
                return str_to_check
            # It is not a palindrome
            if not is_already_checked_non_palin:
                self.non_palin_idxs.add((start_idx, end_idx))
                # Add it's children
                grand_children_ptrs.append((start_idx + 1, end_idx))  # type: ignore
                grand_children_ptrs.append((start_idx, end_idx - 1))  # type: ignore

        return self.get_longest_palin_among_children(children_ptrs=grand_children_ptrs)

    def longestPalindrome(self, s: str) -> str:
        self.input_str = s
        self.non_palin_idxs = set()
        len_s = len(s)
        if len_s <= 1:
            return s

        if self.is_palindrome(s, len_s):
            return s

        children = [(0, len_s - 2), (1, len_s - 1)]
        return self.get_longest_palin_among_children(children_ptrs=children)


s = Solution()

assert s.is_palindrome("abba", 4) == True
assert s.is_palindrome("bbabb", 5) == True
assert s.is_palindrome("cad", 3) == False
assert s.is_palindrome("a", 1) == True
assert s.longestPalindrome("eabcb") == "bcb"
assert s.longestPalindrome("bb") == "bb"
assert s.longestPalindrome("cbbd") == "bb"
assert s.longestPalindrome("c") == "c"

assert (
    s.longestPalindrome("babaddtattarrattatddetartrateedredividerb")
    == "ddtattarrattatdd"
)

s.longestPalindrome(
    "cyyoacmjwjubfkzrrbvquqkwhsxvmytmjvbborrtoiyotobzjmohpadfrvmxuagbdczsjuekjrmcwyaovpiogspbslcppxojgbfxhtsxmecgqjfuvahzpgprscjwwutwoiksegfreortttdotgxbfkisyakejihfjnrdngkwjxeituomuhmeiesctywhryqtjimwjadhhymydlsmcpycfdzrjhstxddvoqprrjufvihjcsoseltpyuaywgiocfodtylluuikkqkbrdxgjhrqiselmwnpdzdmpsvbfimnoulayqgdiavdgeiilayrafxlgxxtoqskmtixhbyjikfmsmxwribfzeffccczwdwukubopsoxliagenzwkbiveiajfirzvngverrbcwqmryvckvhpiioccmaqoxgmbwenyeyhzhliusupmrgmrcvwmdnniipvztmtklihobbekkgeopgwipihadswbqhzyxqsdgekazdtnamwzbitwfwezhhqznipalmomanbyezapgpxtjhudlcsfqondoiojkqadacnhcgwkhaxmttfebqelkjfigglxjfqegxpcawhpihrxydprdgavxjygfhgpcylpvsfcizkfbqzdnmxdgsjcekvrhesykldgptbeasktkasyuevtxrcrxmiylrlclocldmiwhuizhuaiophykxskufgjbmcmzpogpmyerzovzhqusxzrjcwgsdpcienkizutedcwrmowwolekockvyukyvmeidhjvbkoortjbemevrsquwnjoaikhbkycvvcscyamffbjyvkqkyeavtlkxyrrnsmqohyyqxzgtjdavgwpsgpjhqzttukynonbnnkuqfxgaatpilrrxhcqhfyyextrvqzktcrtrsbimuokxqtsbfkrgoiznhiysfhzspkpvrhtewthpbafmzgchqpgfsuiddjkhnwchpleibavgmuivfiorpteflholmnxdwewj"
)
