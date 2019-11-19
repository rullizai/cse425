print("The Given Matrix Is : ")
Y = [[1, 5, 1, 5, 1, 5],
     [3, 3, 2, 3, 3, 4],
     [2, 3, 4, 4, 3, 2],
     [2, 2, 3, 2, 2, 4],
     [2, 2, 4, 3, 4, 2],
     [4, 4, 4, 4, 2, 3]]

for p in range(len(Y)):
    for q in range(len(Y[p])):
        print(Y[p][q], end=" ")
    print()


largest = []

for i in range(len(Y)):
    for j in range(len(Y[i])):
        if i == 0:
            Y[i][j] = Y[i][j]
            largest.append(Y[i][j])
        elif i > 0 and j == 0:
            if (Y[i][j]) * (Y[i - 1][j + 1]) >= (Y[i][j]) * (Y[i - 1][j]):
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j + 1])
                largest.append(Y[i][j])
            else:
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j])
                largest.append(Y[i][j])

        elif i > 0 and j == 5:
            if (Y[i][j]) * (Y[i - 1][j]) >= (Y[i][j]) * (Y[i - 1][j - 1]):
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j])
                largest.append(Y[i][j])
            else:
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j - 1])
                largest.append(Y[i][j])

        else:
            if (Y[i][j]) * (Y[i - 1][j - 1]) >= (Y[i][j]) * (Y[i - 1][j]) and (Y[i][j]) * (Y[i - 1][j - 1]) >= (
            Y[i][j]) * (Y[i - 1][j + 1]):
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j - 1])
                largest.append(Y[i][j])
            elif (Y[i][j]) * (Y[i - 1][j]) >= (Y[i][j]) * (Y[i - 1][j - 1]) and (Y[i][j]) * (Y[i - 1][j]) >= (
            Y[i][j]) * (Y[i - 1][j + 1]):
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j])
                largest.append(Y[i][j])
            else:
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j + 1])
                largest.append(Y[i][j])

theLargest = largest
print()
print("The Transformed Matrix Is : ")

for p in range(len(Y)):
    for q in range(len(Y[p])):
        print(Y[p][q], end=" ")
    print()
print()
print("The Maximum Value Is : ", max(largest))
print()


X = [[1, 5, 1, 5, 1, 5],
     [3, 3, 2, 3, 3, 4],
     [2, 3, 4, 4, 3, 2],
     [2, 2, 3, 2, 2, 4],
     [2, 2, 4, 3, 4, 2],
     [4, 4, 4, 4, 2, 3]]
Y = X

minimum = []

for i in range(len(Y)):
    for j in range(len(Y[i])):
        if i == 0:
            Y[i][j] = Y[i][j]
        elif i > 0 and j == 0:
            if (Y[i][j]) * (Y[i - 1][j + 1]) <= (Y[i][j]) * (Y[i - 1][j]):
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j + 1])
            else:
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j])

        elif i > 0 and j == 5:
            if (Y[i][j]) * (Y[i - 1][j]) <= (Y[i][j]) * (Y[i - 1][j - 1]):
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j])
            else:
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j - 1])

        else:
            if (Y[i][j]) * (Y[i - 1][j - 1]) <= (Y[i][j]) * (Y[i - 1][j]) and (Y[i][j]) * (Y[i - 1][j - 1]) <= (
            Y[i][j]) * (Y[i - 1][j + 1]):
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j - 1])
            elif (Y[i][j]) * (Y[i - 1][j]) <= (Y[i][j]) * (Y[i - 1][j - 1]) and (Y[i][j]) * (Y[i - 1][j]) <= (
            Y[i][j]) * (Y[i - 1][j + 1]):
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j])
            else:
                Y[i][j] = (Y[i][j]) * (Y[i - 1][j + 1])

        if i == 5:
            minimum.append(Y[i][j])

print("The Transformed Matrix Is : ")


for p in range(len(Y)):
    for q in range(len(Y[p])):
        print(Y[p][q], end=" ")
    print()

print()
print("The Minimum Value Is : ", min(minimum))