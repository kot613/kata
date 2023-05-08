def transpose(M):
    ans = [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]
    return ans


transpose([[1, 2, 3]])
transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])


"""
def transpose(matrix):
    return list(map(list, zip(*matrix)))
"""
