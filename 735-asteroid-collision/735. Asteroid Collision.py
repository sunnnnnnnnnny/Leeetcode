class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # since positive move right and negative move left
        # only when a pair of pos, neg appears will it meet
        # we can mimic is by using a queue to record the elements going right
        # and once meeting the going left elements we can start make collision
        # until it explods
        # time: O(N) space:O(N)
        movingRight = []
        ret = []
        for ast in asteroids:
            if ast<0:
                explod = False
                while movingRight:
                    meets = movingRight[-1]
                    if meets<=-ast:
                        movingRight.pop()
                        if meets == -ast:
                            explod = True
                            break
                    else:
                        explod = True
                        break
                if not explod:
                    ret.append(ast)
            else:
                movingRight.append(ast)
        ret.extend(movingRight)
        return ret