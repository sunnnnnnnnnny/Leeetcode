class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        # the separater will have the space of (1+2+....+b)+ each b+3 (<\>) in total
        # b+4, b+5,..., 2b+3 = (b+4+2b+3)*b/2 = (3b+7)*b/2
        # limit*b = (3b+7)*b/2+len(msg)-(0~b-1) and needs to be less than len(msg)
        # where b range from 0 to limit?
        cur = b = 0
        while 3+len(str(b))*2<limit and cur+len(message)+(3+len(str(b)))*b>limit*b:
            b+=1
            # need to add the len of all 1...b in the notion
            cur += len(str(b))
        ret = []
        i = 0
        if 3+len(str(b))*2<limit:
            for j in range(1, b+1):
                strL = limit- (len(str(j))+3+len(str(b)))
                newS = '%s<%s/%s>' % (message[i:i+strL], j, b)
                # ret.append('%s<%s/%s>' % (message[i:i+strL], j, b))
                ret.append(newS)
                i += strL
        return ret