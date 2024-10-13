class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # pos to right neg to left
        # only pos_i<neg_j will collision, ignore the negative on left
        # using stack to mimic the asteroid going right
        # time:O(N) space:O(N)
        astStack = []
        ret = []
        for ast in asteroids:
            if ast>0:
                astStack.append(ast)
            else:
                remain = True
                while astStack:
                    hit = astStack[-1]
                    if -ast>=hit:
                        astStack.pop()
                        if -ast == hit:
                            remain = False
                            break
                    else:
                        remain = False
                        break
                if remain:
                    ret.append(ast)
        ret.extend(astStack)
        return ret