# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.
def match_ends(words):
    count =0
    for word in words:
        if len(word) >=2: # check this first else will create indexing problems
            if (word[0] == word[-1]):
                count += 1
        else:
            pass
    print(count)
    return


match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])  # , 3)
match_ends(['', 'x', 'xy', 'xyx', 'xx'])  # , 2)
match_ends(['aaa', 'be', 'abc', 'hello'])  # , 1)

# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
def front_x(words):
    list1=[]
    list2=[]

    for word in words:
        if word[0]=='x':
            list1.append(word)
        else:
            list2.append(word)
    list1.sort()
    list2.sort()
    print(list1 + list2)

    return

front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])  # ,['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])  # ,['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])  # ,['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])


# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    srt = sorted(tuples, key= lambda x: x[1])
    print(srt)
    return




sort_last([(1, 3), (3, 2), (2, 1)])#,[(2, 1), (3, 2), (1, 3)])
sort_last([(2, 3), (1, 2), (3, 1)])#,[(3, 1), (1, 2), (2, 3)])
sort_last([(1, 7), (1, 3), (3, 4, 5)]) #, (2, 2)]),[(2, 2), (1, 3), (3, 4, 5), (1, 7)])

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

def remove_adjacent(nums):
    popList=[]
    if len(nums) >2:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                popList.append(i)
    rev = sorted(popList, reverse=True)
    for pop in rev:

        nums.pop(pop)
    print(nums)
    return

remove_adjacent([1, 2, 2, 3]) #, [1, 2, 3])
remove_adjacent([2, 2, 3, 3, 3])  #, [2, 3])
remove_adjacent([]),# [])


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.
def linear_merge(list1, list2):
    # +++your code here+++
    return



linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])#,['aa', 'bb', 'cc', 'xx', 'zz'])
linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz'])#,['aa', 'bb', 'cc', 'xx', 'zz'])
linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb'])#,['aa', 'aa', 'aa', 'bb', 'bb'])

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.






