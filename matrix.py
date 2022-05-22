m = int(input("Enter N for N x N matrix: "))
n = m
matrixA = []
matrixB = []
result = []
print("please enter A matrix rowwise")
for i in range(m):
    elements = []
    for j in range(n):
        elements.append(int(input("entries")))
    matrixA.append(elements)
print("Matrix A : ")
for i in matrixA:
    print(i)    

print("please enter  matrix B rowwise")
for i in range(m):
    elements = []
    for j in range(n):
        elements.append(int(input("entries")))
    matrixB.append(elements)
print("Matrix B : ")
for i in matrixB:
    print(i)

for i in range(m):
    elements = []
    for j in range(n):
        elements.append(0)
    result.append(elements)

for i in range(len(matrixA)):
    for j in range(len(matrixB[0])):
        for k in range(len(matrixB)):
            result[i][j] += matrixA[i][k] * matrixB[k][j]

# for i in range(m):
#     for j in range(n):
#         print(matrixA[i][j], end=" ")
#     print()

# for i in range(m):
#     for j in range(n):
#         print(matrixB[i][j], end=" ")
#     print()

# for i in range(m):
#     for j in range(n):
#         print(result[i][j], end = " ")
#     print()
print("The resultent matrix is : ")
for i in result:
    print(i)
    
