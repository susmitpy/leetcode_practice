
def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    len_nums1 = len(nums1)
    len_nums2 = len(nums2)
    total_length = len_nums1 + len_nums2
    is_even = total_length % 2 == 0
    
    ptr_nums1 = 0
    ptr_nums2 = 0
    
    new_list = []
    while True:
        if ptr_nums1 == len_nums1:
            new_list.extend(nums2[ptr_nums2:])
            break
        
        if ptr_nums2 == len_nums2:
            new_list.extend(nums1[ptr_nums1:])
            break
        
        if nums1[ptr_nums1] <= nums2[ptr_nums2]:
            new_list.append(nums1[ptr_nums1])
            ptr_nums1 += 1
        else:
            new_list.append(nums2[ptr_nums2])
            ptr_nums2 += 1

    if is_even:
        return (new_list[total_length//2] + new_list[total_length//2 - 1]) / 2
    
    return new_list[total_length//2]

nums1 = [1,2]
nums2 = [3,4]

new_list = findMedianSortedArrays(nums1, nums2)
print(new_list)