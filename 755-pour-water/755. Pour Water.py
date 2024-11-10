class Solution:
    def pourWater(self, height: List[int], volume: int, k: int) -> List[int]:
        # record the downward location of the left side, ad its leftBoundary
        # each water will be pour on the leftMost stack, and to update the stack is
        # by adding the -1 to the stack, until it reaches the leftBoundary
        # onve the leftside finishes, go to the rightside
        # time:O(N+V) space:O(N)
        n = len(height)
        leftFall, rightFall, leftBond, rightBond = [], [], k, k
        for s in range(volume):
            while leftBond>0 and height[leftBond-1]<=height[leftBond]:
                leftBond -= 1
                if height[leftBond]<height[leftBond+1]:
                    leftFall.append(leftBond)
            while rightBond<n-1 and height[rightBond+1]<=height[rightBond]:
                rightBond += 1
                if height[rightBond]<height[rightBond-1]:
                    rightFall.append(rightBond)
            if leftFall:
                now = leftFall[-1]
                height[now]+=1
                if height[now]==height[now+1]:
                    leftFall.pop()
                if now>leftBond:
                    leftFall.append(now-1)
            elif rightFall:
                now = rightFall[-1]
                height[now]+=1
                if height[now]==height[now-1]:
                    rightFall.pop()
                if now<rightBond:
                    rightFall.append(now+1)
            else:
                height[k]+=1
                if k>leftBond:
                    leftFall.append(k-1)
                if k<rightBond:
                    rightFall.append(k+1)
        return height
        
            
        