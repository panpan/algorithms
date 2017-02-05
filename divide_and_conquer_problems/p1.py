'''
You are given as input an unsorted array of n distinct numbers, where n
is a power of 2. Give an algorithm that identifies the second-largest
number in the array, and that uses at most n+log(n)-2 comparisons.
'''

def second_largest(A):
    B = largest_compared(A)[1] # O(n-1)
    return largest_compared(B)[0] # O(log(n)-1)

def largest_compared(A): # returns max value and all values compared to it
    if len(A) < 2:
        return A[0], []
    m = len(A)//2
    left, right = largest_compared(A[:m]), largest_compared(A[m:])
    if left[0] > right[0]:
        left[1].append(right[0])
        return left
    else:
        right[1].append(left[0])
        return right
