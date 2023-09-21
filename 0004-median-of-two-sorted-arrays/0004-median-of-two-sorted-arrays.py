class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m, i, j, n1, m1 = len(nums1), len(nums2), 0, 0, 0, 0

        for count in range(0, (n + m) // 2 + 1):
            m1 = n1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    n1 = nums2[j]
                    j += 1
                else:
                    n1 = nums1[i]
                    i += 1
            elif i < n:
                n1 = nums1[i]
                i += 1
            else:
                n1 = nums2[j]
                j += 1

        if (n + m) % 2 == 1:
            return float(n1)
        else:
            ans = float(n1) + float(m1)
            return ans / 2.0