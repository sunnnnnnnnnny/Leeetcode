class Solution:
    def defangIPaddr(self, address: str) -> str:
        # string replace or go through one by one
        # if the input is valid, time:O(N) space:O(N)
        ret = address.replace(".", "[.]")
        # print(ret)
        return ret