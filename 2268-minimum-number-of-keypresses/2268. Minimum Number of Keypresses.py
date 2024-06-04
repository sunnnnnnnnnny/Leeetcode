class Solution:
    def minimumKeypresses(self, s: str) -> int:
        # greedy: count the frequency of all char
        # sort the array of freq
        # assign the high frequency to be one hit
        # thus assign based on the freq to get the min press
        # time: O(N+NlogN+N) space:O(N)
        charCount = {}
        for i in range(len(s)):
            if s[i] not in charCount.keys():
                charCount[s[i]] = 0
            charCount[s[i]] += 1
        # sort the freq from high to low
        cnts = list(charCount.values())
        cnts.sort(reverse=True)
        ret = 0
        keyPressAssign = 1
        keyPressAssignLeft = 9
        for i in range(len(cnts)):
            keyFreq = cnts[i]
            ret += (keyFreq*keyPressAssign)
            keyPressAssignLeft -= 1
            if keyPressAssignLeft == 0:
                keyPressAssign += 1
                keyPressAssignLeft = 9
        return ret


        