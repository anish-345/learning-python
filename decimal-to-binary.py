d = float(input('Enter a decimal no. less than 1 : '))
p = 0
while ((2**p)*d)%1 != 0 :
    print (f"remainder = {str(((2**p)*d) - int(((2**p)*d)))}")
    p += 1
n = int(d*(2**p))
res = ''
if n == 0 :
   res ="0"
while n >0 :
     res = str(n%2) + res
     n = n//2

for i in range (p - len(res)):
     res = '0' + res
               
res = res[0:-p] + '0.' + res[-p:]
print (f"the binary representation of {str(d)} is {str(res)} ")
     
