s = str(input('Enter a string :'))
seen =''

for char in s:
   if char not in seen:
    seen += char
print (seen)
print (f'{len(seen)} unique character in the string')
      
