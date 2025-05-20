matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(matrix)
print(matrix[2][1])
# calculates rows
print(len(matrix))
print(len(matrix[2]))

for x in range(3):
    for y in range(3):
        print(matrix[x][y], end = " ")
    print("\n")