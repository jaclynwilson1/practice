nums1 = [1, 2, 3, 4]
nums2 = [2, 3, 3, 5]
m = 3
n = 4

nums1 = nums1[0:m]
print(nums1)
nums2 = nums2[0:n]

for i in nums2:
    nums1.append(i)

print(nums1)
nums1.sort(reverse=True)
print(nums1)