def findDifference(nums1, nums2):
    answer = [list(set(nums1) - set(nums2)), list(set(nums2) - set(nums1))]
    return answer


# Runtime1 25ms Beats 86.07% of users with Python
# Memory 13.50MB Beats 97.07% of users with Python