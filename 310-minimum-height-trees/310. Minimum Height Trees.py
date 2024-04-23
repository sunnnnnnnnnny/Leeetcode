class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # bruteforcce to try every node as a root
        # by topoligical sotrting trim the leaf node until centroid appears
        # use adjacency list to get the leaf node, the one with len(neighbor) == 1
        if n<=2:
            return [i for i in range(n)]
        # build adjacency list
        neighbors = [set() for i in range(n)]
        for point1, point2 in edges:
            neighbors[point1].add(point2)
            neighbors[point2].add(point1)
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)
        remaining_nodes = n
        while remaining_nodes>2:
            remaining_nodes -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                neighbor_of_leaf = neighbors[leaf].pop()
                neighbors[neighbor_of_leaf].remove(leaf)
                if len(neighbors[neighbor_of_leaf]) == 1:
                    new_leaves.append(neighbor_of_leaf)
            leaves = new_leaves
        return leaves

        