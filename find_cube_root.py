N = abs(int(input('Enter a positive integer : ')))
count = 0
while count**3 < N :
    count += 1
if count**3 == N :
   print (f'cube root of {N} is {count}')
else:
  print (f'{N} is not a perfect cube')
                                           
