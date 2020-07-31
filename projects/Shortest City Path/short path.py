# importing math module so as to use sqrt function
import math
d = dict()
d1 = dict()
# creating static dictionaries
# this is for storing the coordinate value for each city
d1 = {'A': (0, 0), 'B': (11, 6), 'C': (10, -6), 'D': (21, 13),
      'E': (20, -5), 'F': (30, 3), 'G': (40, 12)}
# this is for storing the path mentioned in the graph
d = {0: ['A', 'B', 'C', 'D', 'G'], 1: [
    'A', 'C', 'D', 'G'], 2: ['A', 'B', 'E', 'F', 'D', 'G']}

'''function to calculate distance between two points and this distance is the euclidian
distance.
Euclidian distance between (x1,y1) and (x2,y2) is sqrt((x2-x1)**2 +(y2-y1)**2)
'''


def dist(a, b):
    # a and b are two pair of coordinate value
    # calculation of distance
    d = math.sqrt((b[0]-a[0])**2+(b[1]-a[1])**2)
    return d


# list
dis = []
# iterating over the d dictionary to calculate the total distance
# which will be covered in the respective paths
for i in range(len(d)):
    l = d[i]
    s = 0
    # iterating over the list of cities
    for j in range(len(l)):
        # if the city is not last city
        if(j != len(l)-1):
            s = s+dist(d1[l[j]], d1[l[j+1]])
    # appending the distance of each path of dictionary in the list
    dis.append(s)

# now the minimum value will be selected from dis as the path with minimum distance
# will be the path required for this question
min_value = min(dis)
# index of minimum value will be extracted using this loop
for i in range(len(dis)):
    if(dis[i] == min_value):
        m = i
        break
# printing the path with the shortest distance
print("Shortest Path in the graph is ", end='')
for j in d[i]:
    print(j+" ", end='')
