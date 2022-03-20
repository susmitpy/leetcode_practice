# https://leetcode.com/problems/number-of-digit-one/

from typing import Set


class Solution:
    to_skip: Set[int]

    def countDigitOne(self, n: int) -> int:
        lower_bound_num_digits = len(str(n)) - 1
        count = lower_bound_num_digits * (10 ** (lower_bound_num_digits - 1))
        max_num_of_len_digits = (10 ** lower_bound_num_digits) - 1

        self.to_skip = set()
        for i in range(max_num_of_len_digits + 1, n + 1):
            if i in self.to_skip:
                continue
            str_i = str(i)
            permutations = self.get_permutations(
                min_num=max_num_of_len_digits, max_num=n, unprocessed=str_i
            )
            count_of_one = str_i.count("1")
            if count_of_one > 0:
                count_of_valid_permutations = len(
                    [i for i in permutations if i not in self.to_skip]
                )
                count += count_of_one * count_of_valid_permutations

            self.to_skip.update(permutations)

        return int(count)

    def insert_at_idx(self, s: str, idx: int, val: str) -> str:
        return s[:idx] + val + s[idx:]

    def get_permutations(
        self, min_num: int, max_num: int, unprocessed: str, processed: str = ""
    ) -> Set[int]:
        if unprocessed == "":
            num = int(processed)
            if num <= max_num and num > min_num:
                return {num}
            return set()

        ans = set()
        for idx in range(len(processed) + 1):
            ans.update(
                self.get_permutations(
                    min_num=min_num,
                    max_num=max_num,
                    unprocessed=unprocessed[1:],
                    processed=self.insert_at_idx(processed, idx, unprocessed[0]),
                )
            )

        return ans


s = Solution()

assert s.countDigitOne(99) == 20
assert s.countDigitOne(999) == 300
assert s.countDigitOne(9999) == 4000
assert s.countDigitOne(0) == 0
assert s.countDigitOne(1) == 1
assert s.countDigitOne(30) == 13
assert s.countDigitOne(21) == 13
assert s.countDigitOne(40) == 14
# print(s.countDigitOne(3184191))
