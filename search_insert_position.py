from typing import List

class Solution:
    search_space: List[int]
    lookout_for: int
    len_search_space: int

    def search(self, start: int, end: int) -> int:
        midpoint = (start+end) // 2
        if start > end: 
            return start

        elem = self.search_space[midpoint]
        if elem == self.lookout_for:
            return midpoint
        
        if elem < self.lookout_for:
            return self.search(start=midpoint+1, end=end)

        return self.search(start=start, end=midpoint-1)
        
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.search_space = nums
        self.lookout_for = target
        self.len_search_space = len(nums)

        return self.search(start=0, end=len(nums)-1)


s = Solution()
assert s.searchInsert([1,3,5,6], 5) == 2
assert s.searchInsert([1,3,5,6], 2) == 1
assert s.searchInsert([1,3,5,6], 7) == 4
assert s.searchInsert([1,3,5,6], 0) == 0
assert s.searchInsert([1,3], 0) == 0
assert s.searchInsert([1,3], 2) == 1, s.searchInsert([1,3], 2)
