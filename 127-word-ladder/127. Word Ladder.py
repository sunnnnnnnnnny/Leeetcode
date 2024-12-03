class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # build connection of word1 to w2 with key of masking each char
        # assume no duplicate word in wordList
        # time:O(NM+N) N len wordlist M avg word len, to build the connection
        # N is for bfs traversal
        # space:O(N^2)
        if beginWord == endWord:
            return 0
        w2w = defaultdict(set)
        key2Words = defaultdict(set)
        endWordExist = False
        for w in wordList:
            if w == endWord:
                endWordExist = True
            for i in range(len(w)):
                key = w[:i]+"*"+w[i+1:]
                # print(w, key, key2Words[key])
                for neighbor in key2Words[key]:
                    w2w[w].add(neighbor)
                    w2w[neighbor].add(w)
                    # print(neighbor, w2w[neighbor])
                key2Words[key].add(w)
            
            # print(w, w2w[w])
        if not endWordExist:
            return 0
        visited = set()
        step = 0
        nextV = []
        if beginWord not in w2w:
            step = 1
            for i in range(len(beginWord)):
                key = beginWord[:i]+"*"+beginWord[i+1:]
                # print(i, key, key2Words[key])
                for neighbor in key2Words[key]:
                    if neighbor not in visited:
                        nextV.append(neighbor)
        else:
            nextV.append(beginWord)
        # print(nextV)
        while nextV:
            levelS = len(nextV)
            for i in range(levelS):
                nowW = nextV.pop(0)
                # print(step, i, nowW, w2w[nowW])
                if nowW in visited:
                    continue
                if nowW == endWord:
                    return step+1
                visited.add(nowW)
                for neighbor in w2w[nowW]:
                    if neighbor not in visited:
                        nextV.append(neighbor)
            step += 1
        return 0
