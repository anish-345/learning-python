x = int(input("Enter an integer [x > 1] : "))
e = 0.001
operation = int(input('''For quare root type : 1 : 
 For cube root type : 2 : '''))
# definig the function
def square_root(w, oper):
    #naming variables
    (high, low) = (w, 0)
    guess = (high + low)/2
#setting conditions for operations
    if oper == 1 :
      #operation for getting square root
      while abs(guess**2 - w) >= e:
          print (f"guessing for {guess}")
          if guess**2 < w :
             low = guess 
          else:
             high = guess
          guess = (low + high)/2
      print (f'square root of {w} is {guess}')
    elif oper == 2 :
      #operation for getting cube root
      while abs(guess**3 - w) >= e:
          print (f"guessing for {guess}")
          if guess**3 < w :
             low = guess
          else:
             high = guess
          guess = (low + high)/2
      print (f'cube root of {w} is {guess}')
    else:
      print ("Please select a valid operation")
    return guess
if x > 1:
 square_root(x, operation)
else:
 print ("Please enter integer [x > 1]")
