import matplotlib.pyplot as plt

# Return side of point j with respect to the line segment
def findSide(point1, point2, j):
    val = (j[1] - point1[1]) * (point2[0] - point1[0]) - (point2[1] - point1[1]) * (j[0] - point1[0])
    if val > 0:
        return 1
    if val < 0:
        return -1
    return 0


# Computes the distance between point j and the line segment formed by point1 and point2
# Uses the abs() so that there is no loss in accuracy
def lineDistance(point1, point2, j):  
    return abs((j[1] - point1[1]) * (point2[0] - point1[0]) - (point2[1] - point1[1]) * (j[0] - point1[0]))

def quickHull(x, n, point1, point2):
    maxDistance = 0
    ind = -1

    for i in range(n):
        temp = lineDistance(point1, point2, x[i])
        if findSide(point1, point2, x[i]) == 1 and temp > maxDistance:
            ind = i
            maxDistance = temp

    if ind == -1:
        if point1 not in hull:
            hull.append(point1)
        if point2 not in hull:
            hull.append(point2)
        return
    # Recursive calls for the two partitions
    quickHull(x, n, point1, x[ind])
    quickHull(x, n, x[ind], point2)

# Use matplotlib library to plot the points on a 2D graph
def visualiseHull(x, hull_points):
    
    points_x = [point[0] for point in x]
    points_y = [point[1] for point in x]

    hull_x = [point[0] for point in hull_points]
    hull_y = [point[1] for point in hull_points]

    plt.figure(figsize=(8, 6))
    plt.scatter(points_x, points_y, color='blue', label='Points')
    plt.plot(hull_x + [hull_x[0]], hull_y + [hull_y[0]], color='red', linestyle='-', linewidth=2, label='Convex Hull')

    plt.title('Quick Hull Algorithm - Convex Hull Visualization')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Take values accquired from functions and create the final convex hull
def showHull(x, n):
    global hull
    # If set of points is less than 3 a hull is not possible 
    # as it would just form a line and not a shape
    # n is the number of points where 
    if n < 3:
        print("Convex hull not possible")
        return

    minimumX = 0
    maximumX = 0
    for i in range(1, n):
        if x[i][0] < x[minimumX][0]:
            minimumX = i
        if x[i][0] > x[maximumX][0]:
            maximumX = i

    hull = []
    quickHull(x, n, x[minimumX], x[maximumX])
    quickHull(x, n, x[maximumX], x[minimumX])
    visualiseHull(x, hull)

# Driver code
# Change values to generate different convex hulls
x = [[0, 3], [1, 1], [2, 2], [4, 4],
     [0, 0], [1, 2], [3, 1], [3, 3]]
n = len(x)
showHull(x, n)
