n = int(input("Enter an integer : "))
res =""
if n == 0 :
  res =0
while n > 0 :
   res = str(n%2) + res
   n = n//2
print (res)
                  
