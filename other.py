# Qirui Wang
# Generate graph coloring lpsolve input file
# Python 3.8
#
import math


# # 10 vertex planar graph
# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # the list of integers contains all vertices
# n = 10 # the number of vertices
# # the list of integers contains all vertices
# edges = [[1, 2], [1, 3], [1, 6], [1, 7], [1, 10], [2, 4], [2, 7], [3, 5], [3, 10], [4, 5], [4, 7], [4, 8], [4, 9], [5, 9], [5, 10], [6, 7], [6, 8], [6, 9], [6, 10], [7, 8], [8, 9], [9, 10]]

# # 9 vertex planar graph
# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 9
# edges = [[1, 2], [1, 3], [1, 4], [1, 7], [1, 9], [2, 3], [2, 5], [2, 7], [3, 4], [3, 5], [3, 6], [4, 6], [4, 9], [5, 6], [5, 7], [5, 8], [6, 8], [6, 9], [7, 8], [7, 9], [8, 9]]

# # 6 vertex planar graph
# vertices = [1, 2, 3, 4, 5, 6]
# n = 6
# edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [2, 4], [2, 6], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]]

# # 6 wheel graph
# vertices = [1, 2, 3, 4, 5, 6]
# n = 6
# edges = [[1, 2], [1, 3], [1, 6], [2, 4], [2, 6], [3, 5], [3, 6], [4, 5], [4, 6], [5, 6]]

# # 7 wheel graph
# vertices = [1, 2, 3, 4, 5, 6, 7]
# n = 7
# edges = [[1, 2], [1, 3], [1, 7], [2, 4], [2, 7], [3, 5], [3, 7], [4, 6], [4, 7], [5, 6], [5, 7], [6, 7]]

# # fritsch graph
# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 9
# edges = [[1, 2], [1, 3], [1, 4], [1, 8], [1, 9], [2, 4], [2, 5], [2, 8], [3, 4], [3, 6], [3, 9], [4, 5], [4, 6], [5, 6], [5, 7], [5, 8], [6, 7], [6, 9], [7, 8], [7, 9], [8, 9]]


# # Errera graph
# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
# n = 17
# edges = [[1, 2], [1, 12], [1, 14], [1, 16], [1, 17], [2, 3], [2, 4], [2, 12], [2, 14], [3, 4], [3, 5], [3, 6], [3, 12], [3, 13], [4, 5], [4, 7], [4, 14], [4, 15], [5, 6], [5, 7], [5, 8], [6, 9], [6, 13], [7, 10], [7, 15], [8, 9], [8, 10], [9, 10], [9, 11], [9, 13], [10, 11], [10, 15], [11, 13], [11, 15], [11, 16], [11, 17], [12, 13], [12, 16], [13, 16], [14, 15], [14, 17], [15, 17], [16, 17]]

# # Soifer graph
# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 9
# edges = [[1, 2], [1, 3], [1, 4], [1, 8], [2, 3], [2, 5], [2, 9], [3, 6], [4, 6], [4, 7], [4, 8], [5, 6], [5, 9], [6, 7], [6, 9], [7, 8], [7, 9], [8, 9]]

# Torodial graph v9
# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 9
# edges = [[1, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 5], [3, 6], [4, 5], [4, 6], [5, 7], [5, 8], [5, 9], [6, 7], [6, 8], [6, 9], [7, 8], [7, 9], [8, 9]]

# Torodil graph v10
# vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# n = 10
# edges = [[1, 2], [1, 3], [1, 5], [2, 4], [2, 8], [3, 6], [3, 9], [4, 5], [4, 6], [5, 7], [5, 8], [6, 7], [6, 10], [8, 10], [9, 10]]

# Torodial graph v18
vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
n = 18
edges = [[1, 2], [1, 4], [1, 11], [2, 5], [2, 9], [3, 15], [3, 7], [3, 8], [4, 6], [4, 10], [5, 6], [5, 8], [6, 7], [7, 9], [8, 10], [9, 12], [10, 17], [11, 14], [11, 16], [12, 13], [12, 16], [13, 14], [13, 15], [14, 17], [15, 18], [16, 18], [17, 18]]



### print the objective function
result = "min: "
for i in vertices:
    result = result + "+y_" + str(i)
result = result + ";"
print(result)


# ### print the constraint: all vertices can only colored by one color
for i in vertices:
    result = ""
    for k in vertices:
        result = result + "+x_" + str(i) + "_" + str(k)
    result = result + "=1;"
    print(result)


### print the constraint: a vertex cannot be colored with an unused colored
for i in vertices: 
    for k in vertices:
        print("x_" + str(i) + "_" + str(k) + "<=" + "y_" + str(k) + ";")


### print the constraint: adjacent vertices have different colors
for e in edges:
    for k in vertices:
        print("x_" + str(e[0]) + "_" + str(k) + "+x_" + str(e[1]) + "_" + str(k) + "<=1;")



### Additional constraint: two regions that border the same region cannot be colored the same

extraE = []
for preE in edges:
    p0 = preE[0]
    p1 = preE[1]
    for nextE in edges:
        n0 = nextE[0]
        n1 = nextE[1]
        if p0 == n0 and [p1, n1] not in edges and [n1, p1] not in edges and n1 != p1:
            extraE.append([p1, n1])
        elif p0 == n1 and [p1, n0] not in edges and [n0, p1] not in edges and n0 != p1:
            extraE.append([p1, n0])
        elif p1 == n0 and [p0, n1] not in edges and [n1, p0] not in edges and n1 != p0:
            extraE.append([p0, n1])
        elif p1 == n1 and [p0, n0] not in edges and [n0, p0] not in edges and n0 != p0:
            extraE.append([p0, n0])

    
result = []
for i in extraE:
    if i not in result and [i[1], i[0]] not in result:
        result.append(i)

for e in result:
  for k in vertices:
    print("x_" + str(e[0]) + "_" + str(k) + "+x_" + str(e[1]) + "_" + str(k) + "<=1;")


### print the constraint: we will not use the color if the privious color has been used
for i in range(2, n+1):
    print("y_" + str(i) + "<=" + "y_" + str(i-1) + ";")

### Define binary variables
result = "bin "
for i in vertices:
    for k in vertices:
        result = result + "x_" + str(i) + "_" + str(k) + ", "

for i in vertices:
    result = result + "y_" + str(i) + ","

result = result[0:len(result) - 1] + ";"
print(result)