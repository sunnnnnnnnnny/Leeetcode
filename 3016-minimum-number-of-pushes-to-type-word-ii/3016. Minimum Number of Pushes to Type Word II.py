class Solution:
    def minimumPushes(self, word: str) -> int:
        # greedy always map the high freq char to first
        # with only 8 spots, we need to go through each letter
        # time: O(N+26log26+26) = O(N) for sorting
        # space:O(1) cause we only need 8 key to record the mapping
        maxKey = 8
        # keyCnt = [1]*maxKey
        char2Freq = [0]*26
        for i in range(len(word)):
            letter = ord(word[i])-ord('a')
            char2Freq[letter]+=1
        char2Freq.sort(reverse=True)
        # keyIdx = 0
        ret = 0
        idx = 0
        for freq in char2Freq:
            if freq == 0:
                break
            ret += (freq*(idx//maxKey+1))
            idx += 1
            # ret += (keyCnt[keyIdx]*freq)
            # keyCnt[keyIdx]+=1
            # keyIdx+=1
            # if keyIdx>=maxKey:
            #     keyIdx = 0
        return ret
