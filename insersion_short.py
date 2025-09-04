#shorting function
def mergesort(A, a=0, b = None):
    '''takes 'A' array and return its shorted version , 'a' initial element index , b is last element's index'''
    if b == None:
      b = len(A)
    if 1 < (b - a) :
      #breaking the array into 2
       
       c = (a + b + 1) // 2
       mergesort(A, a, c)
       mergesort(A, c, b)
       L, R = A[a:c], A[c:b]
       i, j = 0, 0
       
       while a < b:
       
          #merging arrays back in 'A'
          if (j >= len(R)) or (i < len(L) and L[i] < R[j]):
                 A[a] = L[i]
                 i += 1
          else:
              A[a] = R[j]
              j += 1
          a += 1
    return A

A = [ 3, 8, 2 ,9, 6]
print (f'unsorted array is : {A}\n')
print (f'shorted array is : {mergesort(A)}')
