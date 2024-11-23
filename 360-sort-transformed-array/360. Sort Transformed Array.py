class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        # the c doesn't make any different
        # calculate the num based on the formula and sort? O(NlogN)
        # since knowing the x^2 + x will form a parabola., we can find the part of neg and pos
        # going to neg first then pos based on the f(x) with 2 pointers
        # Positive A means the parabola remains concave (high-low-high), 
        # but negative A inverts the parabola to be convex (low-high-low).
        # time:O(N)
        left = 0
        right = len(nums)-1
        n = len(nums)
        ret = []
        def getForm(x):
            return a*x*x+b*x+c
        if a >=0 :
            # high -low-high or a straight line, get the bigger one
            while left<=right:
                leftX = getForm(nums[left])
                rightX = getForm(nums[right])
                if leftX>rightX:
                    ret.append(leftX)
                    left += 1
                elif leftX<rightX:
                    ret.append(rightX)
                    right -= 1
                else:
                    ret.append(leftX)
                    left += 1
                    if left<right:
                        ret.append(rightX)
                        right -= 1 
            ret = ret[::-1]
        else:
             #low - high -low, put the smaller first
            while left<=right:
                leftX = getForm(nums[left])
                rightX = getForm(nums[right])
                if leftX<rightX:
                    ret.append(leftX)
                    left += 1
                elif leftX>rightX:
                    ret.append(rightX)
                    right -= 1
                else:
                    ret.append(leftX)
                    left += 1
                    if left<right:
                        ret.append(rightX)
                        right -= 1

        return ret
        