'''
You are given an n by n grid of distinct numbers. A number is a local
minimum if it is smaller than all of its neighbors. (A neighbor of a
number is one immediately above, below, to the left, or the right. Most
numbers have four neighbors; numbers on the side have three; the four
corners have two.) Use the divide-and-conquer algorithm design paradigm
to compute a local minimum with only O(n) comparisons between pairs of
numbers.
'''

def find_min(A):
    inf = float('inf')
    l = len(A)+2
    B = [[inf] * l] + [[inf] + row + [inf] for row in A] + [[inf] * l]
    return _find_min(B, 1)

def _find_min(B, n):
    l = len(B)
    if n >= l/2:
        return

    box = [[i,j] for i in range(n,l-n) for j in range(n,l-n)
        if i==n or j==n or i==l-n-1 or j==l-n-1]
    for i,j in box:
        if is_min(B, i, j):
            return i-1,j-1

    return _find_min(B, n+1)

def is_min(B, i, j):
    return B[i][j] < B[i-1][j] and B[i][j] < B[i+1][j] \
        and B[i][j] < B[i][j-1] and B[i][j] < B[i][j+1]
