'''
Quicksort with choice of pivot
    p = 1: first element
    p = 2: last element
    p = 3: median-of-three for first, middle, and last elements

returns total number of comparisons (excluding when choosing the median)
'''

A = [int(line.rstrip('\n')) for line in open('QuickSort.txt')]

def quicksort(A, p):
    return _quicksort(A, 0, len(A)-1, p)

def _quicksort(A, l, r, p):
    count = 0
    if l < r:
        idx, count = partition(A, l, r, p)
        count += _quicksort(A, l, idx-1, p)
        count += _quicksort(A, idx+1, r, p)
    return count

def partition(A, l, r, p):
    swap_pivot(A, l, r, p)
    pivot = A[l]
    i = l+1
    for j in range(l+1, r+1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[l], A[i-1] = A[i-1], A[l]
    return i-1, r-l

def swap_pivot(A, l, r, p):
    if p == 2:
        A[l], A[r] = A[r], A[l]
    elif p == 3:
        m = (l+r)//2
        i = median(A, l, m, r)
        if i == m:
            A[l], A[m] = A[m], A[l]
        elif i == r:
            A[l], A[r] = A[r], A[l]

def median(A, l, m, r):
    if A[l] < A[m]:
        if A[m] < A[r]:
            return m
        elif A[l] < A[r]:
            return r
        else:
            return l
    else:
        if A[l] < A[r]:
            return l
        elif A[m] < A[r]:
            return r
        else:
            return m
