class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        # use 3 pointers always move the smallest one, only when all num same
        # move all 3 pointers, time:O(min(N,M,L)), sapce:O(1)
        a,b,c = 0,0,0
        ret = []
        while a<len(arr1) and b<len(arr2) and c<len(arr3):
            if arr1[a]==arr2[b]==arr3[c]:
                ret.append(arr1[a])
                a+=1
                b+=1
                c+=1
            else:
                minN = min(arr1[a],arr2[b],arr3[c])
                if arr1[a]==minN:
                    a+=1
                if arr2[b]==minN:
                    b+=1
                if arr3[c]==minN:
                    c+=1
        return ret