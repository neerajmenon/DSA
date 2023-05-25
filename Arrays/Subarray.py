#LC-513 


# An efficient program
# to print subarray
# with sum as given sum
 
# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result.
 
 
def subArraySum(arr, sum_):
    n = len(arr)
    currentSum = arr[0]
    l = 0
    r = 1
    while r <= n:
        while currentSum > sum_ and l < r-1:
            currentSum = currentSum - arr[l]
            l += 1
        if currentSum == sum_:
            print("Sum found between indexes %d and %d" % (l, r-1))
            return 1
        if r < n:
            currentSum = currentSum + arr[r]
        r += 1
    print("No subarray found")
    return 0


#with negatives too
def subarray_sum(arr, target_sum):
    prefix_sum = 0
    sum_count = {0: -1}  # A hashmap to store the cumulative sum and its index

    for i, num in enumerate(arr):
        prefix_sum += num
        # Check if there is a subarray with sum equal to target_sum
        if prefix_sum - target_sum in sum_count:
            start = sum_count[prefix_sum - target_sum] + 1
            end = i
            return arr[start:end+1]
        
        # Update the frequency of the current cumulative sum
        sum_count[prefix_sum] = i

    return None  # No subarray found



#maximum subarray sum 
 
class Solution(object):
    def maxSubArray(self, nums):
        currentMax = nums[0]
        maxSoFar = nums[0]
        for i in range(1,len(nums)):
            currentMax += nums[i]
            if currentMax < nums[i]:
                currentMax = nums[i]
            if maxSoFar < currentMax:
                maxSoFar = currentMax
        return maxSoFar
    
#Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#Output: [3,3,5,5,6,7]
class Solution:
    def maxSlidingWindow(self, nums, k):
        if len(nums) == 0:
            return []
        if len(nums) <= k:
            return [self.getMax(nums, 0, k - 1)]
        res = []

        for i in range(len(nums) - k + 1):
            res.append(self.getMax(nums, i, i + k - 1))
        return res
    
    def getMax(self, arr, l, r):
        maximum = arr[l]
        for i in range(l, r + 1):
            maximum = max(arr[i], maximum)
        return maximum


    
"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class Solution(object):
    def subarraySum(self,nums, k):
        count = 0
        current_sum = 0
        sum_count = {0: 1}  # A hashmap to store the cumulative sum frequencies

        for num in nums:
            current_sum += num
            # Check if there is a subarray with sum equal to k
            if current_sum - k in sum_count:
                count += sum_count[current_sum - k]
            
            # Update the frequency of the current cumulative sum
            if current_sum in sum_count:
                sum_count[current_sum] += 1
            else:
                sum_count[current_sum] = 1

        return count
    
# Subarray Sum
def subarraySum(self, nums, k):
    d = {}
    d[0] = 1
    s = 0
    count = 0
    for i in range(len(nums)):
        s += nums[i]
        if s-k in d:
            count += d[s-k]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    
    return count