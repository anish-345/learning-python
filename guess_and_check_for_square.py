guess = 0
x = int(input('Enter an integer :'))
while guess**2 < x:
      guess += 1
                 
if guess**2 == x :
      print (f'square root  of {x} is {guess}')
else:
      print (f"{x} is not a perfect square")
                 
