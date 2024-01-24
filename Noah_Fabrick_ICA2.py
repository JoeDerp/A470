def factorial2(num):
    fact = 1
    for i in range(num):
        fact = fact * (i+1)
    print(fact)

factorial2(10)

def matrixMult(mat1, mat2):
    mat3 = [];
    row1 = len(mat1)
    col1 = len(mat1[0])
    row2 = len(mat2)
    col2 = len(mat2[0])

    if col1 != row2:
        print("Matrix sizes not compatible")
        return
    
    for row in range(row1):
        mat3.append([])
        for col in range(col2):
            mat3[row].append(0)
            for i in range(col2):
                mat3[row][col] += mat1[row][i] * mat2[i][col]
    print(mat3)

mat1 = [[1,2,3,1],[3,2,1,0],[2,2,2,5]]
mat2 = [[4,4,4],[1,2,3],[3,1,1],[2,9,9]]
matrixMult(mat1,mat2)

# Part 3
mass = [1.7, 4.2, 2.6, 5.4]
value = [2, 3, -1, 5]
mv = [round(x[0]*x[1],1) for x in zip(mass,value)]
print(mv)