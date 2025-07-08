#song = ("I threw a wish in the well Dont ask me Ill never tell I looked to you as it fell And now youre in my way  Id trade my soul for a wish Pennies and dimes for a kiss I wasnt looking for this But now youre in my way  Your stare was holdin Ripped jeans skin was showin Hot night wind was blowin Where do you think youre going baby  Hey I just met you And this is crazy But heres my number So call me maybe  Its hard to look right At you baby But heres my number So call me maybe  Hey I just met you And this is crazy But heres my number So call me maybe  And all the other boys Try to chase me But heres my number So call me maybe  You took your time with the call I took no time with the fall You gave me nothing at all But still youre in my way  I beg and borrow and steal Have foresight and its real I didnt know I would feel it But its in my w.lower()).split()
#converting string to frequancy dictionary
song= (input("enter lyrics of song").lower()).split()
def word_frequency(song):
  dict = {}
  for w in song:
     if w in dict:
       dict[w] += 1
     else:
       dict[w] = 1
  return dict
#list all words with same frequency

def most_frequent(dict):
     high=max(dict.values())
     words =[]
     for k, v in dict.items():
         if v == high:
            words.append(k)
     return (words, high)

#getting eords eith freq greater than x

def wrods_with(dic , x=1):
    freq_list=[]
    freq_touple = most_frequent(dic)
    while freq_touple[1] >= x:
          freq_touple= most_frequent(dic)
          freq_list.append(freq_touple)
          for w in freq_touple[0]:

            del(dic[w])

    return freq_list


print (wrods_with(word_frequency(song), 2))
