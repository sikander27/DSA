def findMedianSortedArrays(nums1, nums2):
    nums1.extend(nums2)
    nums1.sort()
    print(m)
    m = len(nums1)//2
    if len(nums1) % 2 == 0:
        print(nums1[m-1] + nums1[m])
        print((nums1[m-1] + nums1[m]) / 2)
    else:
        print( nums1[m])

findMedianSortedArrays([1,3], [2])