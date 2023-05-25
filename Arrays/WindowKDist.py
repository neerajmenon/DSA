class Solution:
    def subarraysWithKDistinct(self, A, K):
        return self.atMostKDistinct(A, K) - self.atMostKDistinct(A, K - 1)
    
    def atMostKDistinct(self, A, K):
        window_counts = {}
        left = 0
        count = 0
        
        for right in range(len(A)):
            # Add the current element to the window
            window_counts[A[right]] = window_counts.get(A[right], 0) + 1
            
            # Shrink the window until the number of distinct elements is <= K
            while len(window_counts) > K:
                window_counts[A[left]] -= 1
                if window_counts[A[left]] == 0:
                    del window_counts[A[left]]
                left += 1
            
            # Count the subarrays ending at the current index
            count += right - left + 1
        
        return count
