class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # kind like a tree with branches being the character the number represents
        # if we enumerate all the possible the 
        # time:O(4^N*N) space:O(N) which does not include the space for solution
        def digit2char(d):
            if d==2:
                return ["a","b","c"]
            elif d==3:
                return ["d","e","f"]
            elif d==4:
                return ["g","h","i"]
            elif d==5:
                return ["j","k","l"]
            elif d==6:
                return ["m","n","o"]
            elif d==7:
                return ["p","q","r","s"]
            elif d==8:
                return ["t","u","v"]
            elif d==9:
                return ["w","x","y","z"]
            return []
        prev = [""]
        ret = []
        for i in range(len(digits)):
            ret = []
            addChar = digit2char(int(digits[i]))
            for c in addChar:
                for p in prev:
                    ret.append(p+c)
            prev = ret
        return ret