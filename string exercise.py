def DrEvil(amt):
    print(amt, "dollars", end=' ')
    if amt == 1000000:
        print('(pinky)')
    else:
        print()
    return None

DrEvil(10)
DrEvil(1000000)

# A. donuts
# Given an int count of a number of donuts, return a string
# of the form 'Number of donuts: <count>', where <count> is the number
# passed in. However, if the count is 10 or more, then use the word 'many'
# instead of the actual count.
# So donuts(5) returns 'Number of donuts: 5'
# and donuts(23) returns 'Number of donuts: many'
def donuts(number):
    x = number
    print('Number of donuts: ', end='')
    if x >=10:
        print('Many')
    else:
        print(x)
    return



donuts(9) # , 'Number of donuts: 9')
donuts(10) #, 'Number of donuts: many')



# B. both_ends
# Given a string s, return a string made of the first 2
# and the last 2 chars of the original string,
# so 'spring' yields 'spng'. However, if the string length
# is less than 2, return instead the empty string.
def both_ends(s):
    if len(s)>2:
        print(s[:2]+s[-2:])
    else:
        print()
    return

both_ends('spring')#, 'spng')
both_ends('Hello')#, 'Helo')
both_ends('a')#, '')
both_ends('xyz')#, 'xyyz')


# C. fix_start
# Given a string s, return a string
# where all occurences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(stra, strb) returns a version of string s
# where all instances of stra have been replaced by strb.
def fix_start(s):
    firstchar=s[0]
    x = s[1:].replace(firstchar,'*')
    if x == '':
        print(s)
    else:
        print(firstchar + x)
    return


fix_start('babble')  #, 'ba**le')
fix_start('aardvark') #, 'a*rdv*rk')
fix_start('google')  #, 'goo*le')
fix_start('donut')   #, 'donut')

# D. MixUp
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_up(a, b):

    print(b[:2]+ a[2:], a[:2] + b[2:] )

    return
#

mix_up('mix', 'pod')#, 'pox mid')
mix_up('dog', 'dinner')#, 'dig donner')
mix_up('gnash', 'sport')#, 'spash gnort')
mix_up('pezzy', 'firm')#, 'fizzy perm')




# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    if len(s) >3 and 'ing' in s:
        print(s + 'ly')
    elif len(s) > 3:
        print(s +'ing')
    else:
        print(s)
    return


verbing('hail')  #  'hailing')
verbing('swiming')  #  'swimingly')
verbing('do')  #  'do')

# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
    if ('not' in s) and ('bad' in s):
        firstIndex=s.find('not')
        lastIndex =s.find('bad')
        if firstIndex < lastIndex:
            print(s[0:firstIndex] + 'good')
        else:
            print(s)
    else:
        print(s)
    return




not_bad('This movie is not so bad')  #  'This movie is good')
not_bad('This dinner is not that bad!')  #  'This dinner is good!')
not_bad('This tea is not hot')  #  'This tea is not hot')
not_bad("It's bad yet not")# "It's bad yet not")

# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  return







# front_back('abcd', 'xy')  #  'abxcdy')
# front_back('abcde', 'xyz')  #  'abcxydez')
# front_back('Kitten', 'Donut')  #  'KitDontenut')












