import numpy as np

def partition(matrix):
    row,col = matrix.shape
    A = matrix[:int(row/2),:int(col/2)] # Top right
    B = matrix[:int(row/2),int(col/2):] # Top left
    C = matrix[int(row/2):,:int(col/2)] # Bottom left
    D = matrix[int(row/2):,int(col/2):] # Bottom right

    return A,B,C,D

def matrixMultiplication(matrix1,matrix2):

    # Assume both matrices are nxn

    n = len(matrix1)

    if n == 1: #1x1 matrix
        return matrix1 * matrix2
    
    A,B,C,D = partition(matrix1) # Notation is from top right to top left, to bottom left to bottom right
    E,F,G,H = partition(matrix2) # Notation is from top right to top left, to bottom left to bottom right

    P1 = matrixMultiplication(A,(F-H))
    P2 = matrixMultiplication((A+B),H)
    P3 = matrixMultiplication((C+D),E)
    P4 = matrixMultiplication(D,(G-E))
    P5 = matrixMultiplication((A+D),(E+H))
    P6 = matrixMultiplication((B-D),(G+H))
    P7 = matrixMultiplication((A-C),(E+F))

    resultA = P5 + P4 - P2 + P6
    resultB = P1 + P2
    resultC = P3 + P4
    resultD = P1 + P5 - P3 - P7


    return np.vstack((np.hstack((resultA,resultB)),np.hstack((resultC,resultD)))) # Create the result matrix by stacking







