class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # rotate layer by layer
        # time:O(N*N) space:O(1) a temp variable to store the rotation
        # math is hard damn
        N = len(matrix)-1
        # start with each layer
        for layer in range(N):
            layerLen = N-layer
            # print('layer: layerLen', layer, layerLen)
            for idx in range(layer, layerLen, 1):
                temp = matrix[layer][idx]
                # print('left up:', layer, idx)
                # left up 
                matrix[layer][idx] = matrix[layerLen-(idx-layer)][layer]
                # left down 
                # print('left down:', layerLen-(idx-layer), layer)
                matrix[layerLen-(idx-layer)][layer] = matrix[layerLen][layerLen-(idx-layer)]
                # right down 
                # print('right down:', layerLen, layerLen-(idx-layer))
                matrix[layerLen][layerLen-(idx-layer)] = matrix[idx][layerLen]
                # right up 
                # print('right up:', idx, layerLen)
                matrix[idx][layerLen] = temp
                # print(matrix)
        return
            

                

        