# Qirui Wang
# Generate graph coloring lpsolve input file
# Python 3.8
#
import math

# the list of integers contains all vertices
vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

# the number of vertices
n = 16

# the list of list contains all edges which are in form of a 2 integer list.
edges = [[1, 2], [1, 3], [1, 4], [1, 5], [2, 3], [3, 4], [4, 5], [2,
                                                                  4], [2, 6],
         [2, 7], [2, 8], [4, 8], [4, 9], [5, 9], [6, 10], [6, 11], [6, 7],
         [7, 8], [8, 9], [10, 16], [10, 15], [10, 11], [7, 11], [7, 12],
         [7, 13], [8, 13], [8, 14], [9, 14], [15, 16], [11, 15], [12, 15],
         [11, 12], [12, 13], [13, 14]]

### print the objective function
result = "min: "
for i in vertices:
    result = result + "+y_" + str(i)
result = result + ";"
print(result)

### print the constraint: all vertices can only colored by one color
for i in vertices:
    result = ""
    for k in vertices:
        result = result + "+x_" + str(i) + "_" + str(k)
    result = result + "=2;"
    print(result)

### print the constraint: a vertex cannot be colored with an unused colored
for i in vertices:
    for k in vertices:
        print("x_" + str(i) + "_" + str(k) + "<=" + "y_" + str(k) + ";")

### print the constraint: adjacent vertices have different colors
for e in edges:
    for k in vertices:
        print("x_" + str(e[0]) + "_" + str(k) + "+x_" + str(e[1]) + "_" +
              str(k) + "<=1;")

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
for i in range(2, n + 1):
    print("y_" + str(i) + "<=" + "y_" + str(i - 1) + ";")

result = "bin "
for i in vertices:
    for k in vertices:
        result = result + "x_" + str(i) + "_" + str(k) + ", "

for i in vertices:
    result = result + "y_" + str(i) + ","

result = result[0:len(result) - 1] + ";"
print(result)
