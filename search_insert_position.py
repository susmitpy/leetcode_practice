from typing import List
from math import ceil

class Solution:
    search_space: List[int]
    lookout_for: int
    len_search_space: int

    def search(self, left_idx: int, right_idx: int):
        if right_idx < 0:
            return 0

        middle_point = ceil((right_idx+left_idx)/2)

        if middle_point >= self.len_search_space:
            return middle_point

        middle_elem = self.search_space[middle_point]
        if middle_elem == self.lookout_for:
            print("Target Found")
            return middle_point

        if left_idx == right_idx:
            print("Target Not Found")

            curr_one_is_greater = self.search_space[left_idx] > self.lookout_for
            if curr_one_is_greater:
                return left_idx
            else:
                return left_idx+1

        if middle_elem > self.lookout_for:
            return self.search(left_idx, middle_point-1)

        return self.search(middle_point+1, right_idx)

    def searchInsert(self, nums: List[int], target: int) -> int:
        self.search_space = nums
        self.lookout_for = target
        self.len_search_space = len(nums)

        return self.search(0, len(nums)-1)


s = Solution()

assert s.searchInsert([1,3,5,6], 5) == 2
assert s.searchInsert([1,3,5,6], 2) == 1
assert s.searchInsert([1,3,5,6], 7) == 4
assert s.searchInsert([1,3,5,6], 0) == 0
assert s.searchInsert([1,3], 0) == 0
assert s.searchInsert([1,3], 2) == 1, s.searchInsert([1,3], 2)
s.searchInsert([1,2,4,6,7], 3)
s.searchInsert([3,5,7,9,10], 8)
s.searchInsert([1,3],4)
