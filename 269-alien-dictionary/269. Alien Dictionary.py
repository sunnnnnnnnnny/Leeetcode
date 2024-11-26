class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # need to make connections of the words
        # creating a tree based on the word will take (n-1) pairs, with each l size => O(NL)
        # getting the order can be done be inorder degree of each character =>O(L) 
        # overall time is O(NL)
        # space:O(N+L) for connections and unique characters
        # since the unique char is fixed to be 26, the time:O(M) of M is the total length of all words
        # space:O(U+min(U^2,N)) U is the unique char with N of words = O(U) = O(1)
        charConnect = defaultdict(set)
        charIndegree = {c:0 for w in words for c in w}
        # print(charIndegree)
        # in_degree = Counter({c: 0 for word in words for c in word})
        # print(in_degree)
        for w1, w2 in zip(words, words[1:]):
            for a, b in zip(w1, w2):
                if a!=b:
                    # add the linakge
                    if b not in charConnect[a]:
                        charConnect[a].add(b)
                        charIndegree[b]+=1
                    break
            else:
                # making sure if b is not a prefix of a
                if len(w1)>len(w2):
                    # print(w1, w2)
                    return ""
        # print(charIndegree)
        # print(charConnect)
        startQ = [k for k in charIndegree.keys() if charIndegree[k] == 0]
        # print(startQ)
        ret = []
        while startQ:
            now = startQ.pop(0)
            ret.append(now)
            for nextchar in charConnect[now]:
                charIndegree[nextchar] -= 1
                if charIndegree[nextchar] == 0:
                    startQ.append(nextchar)
        # print(ret)
        retStr = "".join(ret)
        return "" if len(ret)<len(charIndegree.keys()) else retStr