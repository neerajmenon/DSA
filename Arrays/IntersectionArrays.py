#LC-350 
#Intersection of two arrays II 

#Given two integer arrays nums1 and nums2, return an array of their intersection.
#Each element in the result must appear as many times as it shows in both arrays 
#and you may return the result in any order.

#Follow up:
#What if the given array is already sorted? How would you optimize your algorithm?
#What if nums1's size is small compared to nums2's size? Which algorithm is better?
#What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

class Solution(object):
    def intersect(self, nums1, nums2):
        counts = dict()
        for i in nums1:
            counts[i] = counts.get(i, 0) + 1
        res = []
        for i in nums2:
            if counts.get(i) > 0:
                res.append(i)
                counts[i] -= 1
        return res