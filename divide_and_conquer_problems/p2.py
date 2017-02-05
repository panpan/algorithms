'''
You are a given a unimodal array of n distinct elements, meaning that
its entries are in increasing order up until its maximum element, after
which its elements are in decreasing order. Give an algorithm to compute
the maximum element that runs in O(log n) time.
'''

def maximum(A):
    if len(A) < 2:
        return A[0]
    m = len(A)//2
    B, C = A[:m], A[m:]
    if B[-1] > C[0]:
        return maximum(B)
    else:
        return maximum(C)
