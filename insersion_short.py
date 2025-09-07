#shorting function
def mergesort(A):
    for i in range (1, len(A)):
        j = i 
        while j > 0 and A[j] < A[j - 1]:
             A[j -1], A[j] = A[j], A[j-1]
             j = j-1

    '''takes 'A' array and return its shorted version , 'a' initial element index , b is last element's index'''
    return A

A = [ 3, 8, 2 ,9, 6]
print (f'unsorted array is : {A}\n')
print (f'shorted array is : {mergesort(A)}')
