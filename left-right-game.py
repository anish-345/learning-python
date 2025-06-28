n = 0
where = input('go left or right : ')
while where == 'right' :
      n += 1
      if n < 2 :
        print(':(')
        where = input('go left or right : ')
      if n >= 2:
         print('more than two rights')
         break
print ('you got out')

