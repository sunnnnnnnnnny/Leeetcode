class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        # making it as a json can work
        # but for general split indicator is hard to distinguish with valid ASCII
        # the modification for escapted character will be a good way
        # such as /: and if original str having it then we'll be //:
        # time: O(N), space:O(N)
        # 2. add the length information to the delimiter
        # ex. 5/:
        encodeStr = ""
        for eachStr in strs:
            replaceDelim = eachStr.replace("\:", "\\\:")
            encodeStr = encodeStr+str(len(replaceDelim))+"\:"+replaceDelim
        return encodeStr

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        retStr = []
        idx = 0
        while idx<len(s):
            idxDelim = s.find("\:", idx)
            if idxDelim == -1:
                break
            # print('idx: idxDeli:', idx, idxDelim)
            strLen = s[idx:idxDelim]
            eachStr = s[idxDelim+2:idxDelim+1+int(strLen)+1]
            eachStr = eachStr.replace("\\\:", "\:")
            retStr.append(eachStr)
            idx = idxDelim+1+int(strLen)+1
        return retStr


        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))