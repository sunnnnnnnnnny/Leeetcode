class Solution:
    def alienOrder(self, words: List[str]) -> str:
        # using tree to record the sequence
        # maintain the root nodes and edge of parent -> child
        # if a cycle appear meaning we have conflict order
        adj_list = defaultdict(set)
        in_degree = Counter({c: 0 for word in words for c in word})

        for word1, word2 in zip(words, words[1:]):
            for a, b in zip(word1, word2):
                if a!=b:
                    if b not in adj_list[a]:
                        adj_list[a].add(b)
                        # record how many parents of b
                        in_degree[b] += 1
                    break
            else:
                if len(word1)>len(word2):
                    return""
        ret = []
        # start with the degree of 0 to traverse, bfs
        queue = deque([c for c in in_degree if in_degree[c] == 0])
        while queue:
            now = queue.popleft()
            ret.append(now)
            for b in adj_list[now]:
                in_degree[b] -= 1
                # only the parents are removed, will this node be added
                if in_degree[b] == 0:
                    queue.append(b)
        # if there's more char in the in_degree, meaning having cycle for conflict
        # print(adj_list)
        if len(ret)<len(in_degree):
            return ""
        return "".join(ret)

        