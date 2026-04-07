class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergedArray = []
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0

        if n == 0 and m == 0:
            return 0.0
        while i <n and j<m:
            if nums1[i] < nums2[j]:
                mergedArray.append(nums1[i])
                i += 1
            else:
                mergedArray.append(nums2[j])
                j +=1
        while i< n :
           mergedArray.append(nums1[i])
           i += 1
        while j < m:
           mergedArray.append(nums2[j])
           j += 1

        k = len(mergedArray)
        if k % 2 == 0:
            mid1 = mergedArray[k//2 - 1]
            mid2 = mergedArray[k//2]
            return (mid1 + mid2) / 2

        else:
            return float(mergedArray[k//2])
