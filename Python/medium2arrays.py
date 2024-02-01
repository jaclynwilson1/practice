def findMedianSortedArray(nums1, nums2):
    #given two sorted arrays nums1 & nums2
    #of size m & n, return the median of the two arrays
    joinedList = nums1 + nums2
    joinedList.sort()
    if len(joinedList) == 0:
        median = 0
    if len(joinedList)%2 == 1:
        location = len(joinedList)//2
        median = joinedList[location]
    else:
        location1 = int((len(joinedList)/2) - 1)
        location2 = int((len(joinedList)/2))
        sum = joinedList[location1] + joinedList[location2]
        median = sum/2
    return median

l1 = [1, 3]
l2 = [2]
med1 = 2.0000
total1 = findMedianSortedArray(l1, l2)
print(total1)

l1 = [1,2]
l2 = [3,4]
med2 = 2.5
total2 = findMedianSortedArray(l1, l2)
print(total2)