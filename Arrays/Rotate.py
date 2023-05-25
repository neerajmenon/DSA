class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self,A,D,N):
        D = D%N
        tmp = []
        for i in range(D):
            tmp.append(A.pop(0))
        A.extend(tmp)