li = [int(l.rstrip('\n')) for l in open('IntegerArray.txt')]

def count_inversions(li):
    return msort_count(li)[1]

def msort_count(li): # mergesorts and counts inversions
    if len(li) < 2:
        return li, 0
    m = len(li) // 2
    A, x = msort_count(li[:m])
    B, y = msort_count(li[m:])
    res, z = merge_count(A, B)
    return res, x+y+z

def merge_count(A, B): # merges and counts split inversions
    res = []
    i, j = 0, 0
    count = 0
    while i < len(A) and j < len(B):
        if A[i] <= B[j]:
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            count += len(A) - i
            j += 1
    res += A[i:] + B[j:]
    return res, count
