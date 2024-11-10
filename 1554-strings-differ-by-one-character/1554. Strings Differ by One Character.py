class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        # create Trie with traversing the words
        # time:O(N*M^M) M is the length of each word
        # space:O(N*M)
        # using sring hashing
        # without checking the collision, its going to be time:O(N*M)
        # space:O(N*M)
        n= len(dict)
        m = len(dict[0])
        hash = [0]*n
        MOD = 10**11 + 7
        for i in range(n):
            for j in range(m):
                hash[i] = (26*hash[i]+(ord(dict[i][j])-ord('a')))%MOD
        
        base = 1
        for j in range(m-1, -1, -1):
            seen = set()
            for i in range(n):
                # check each dict[i][j] if it become anything, would it match
                nowHash = (hash[i]-base*(ord(dict[i][j])-ord('a')))%MOD
                if nowHash in seen:
                    return True
                seen.add(nowHash)
            base = 26*base%MOD
        return False
        # trie = defaultdict()
        # def checkInTrie(leftWord, head):
        #     prev = head
        #     for c in leftWord:
        #         if c in prev:
        #             prev = prev[c]
        #         else:
        #             return False
        #     return True
        # def checkDiff(word):
        #     nonlocal trie
        #     prev = trie
        #     needAdd = True
        #     skip = 0
        #     # could match in both direction
        #     for i in range(len(word)):
        #         if word[i] in prev:
        #             prev = prev[word[i]]
        #         else:
        #             skip+=1
        #             print(word, i, skip, word[i+1:], prev)
        #             if skip == 1:

        #                 for child in prev.keys():
        #                     if checkInTrie(word[i+1:], prev[child]):
        #                         print(word, i, word[i+1:], child)
        #                         needAdd = False
        #                         break
        #             else:
        #                 break
        #     print(word, needAdd)
        #     prev = trie
        #     if needAdd:
        #         for i in range(len(word)):
        #             if word[i] not in prev:
        #                 prev[word[i]] = defaultdict()
        #             prev = prev[word[i]]
        #     return not needAdd
        # for nowword in dict:
        #     if checkDiff(nowword):
        #         return True
        # return False
                
