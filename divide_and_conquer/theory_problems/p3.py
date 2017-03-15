'''
You are given a sorted (from smallest to largest) array A of n distinct
integers which can be positive, negative, or zero. You want to decide
whether or not there is an index i such that A[i] = i. Design the
fastest algorithm that you can for solving this problem.
'''

def idx_val_match(A, i=0): # O(log n)
    if len(A) < 2:
        return A[0] == i
    m = len(A)//2
    if A[m] > i+m:
        return idx_val_match(A[:m], i)
    else:
        return idx_val_match(A[m:], i+m)
