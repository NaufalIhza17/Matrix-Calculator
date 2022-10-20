'''
    10 / 17 / 2022

    Made by :   Mochammad Naufal Ihza Syahzada
    NRP     :   5025211260

    This program include the solution of,
    -> determinan   [V]
    -> inverse      [V]
'''

import os
import time

# MAIN FUNCTION
def main():
    
    clear()

    while True:
        n = intro()

        if n == 0:
            clear()
            print("\nTHANKS!\n")
            break

        rows = int(input("Insert row of your matrix: "))

        matrix = []

        for i in range(rows):
            element = input(f"Insert element matrix row {i}: ")
            element_split = element.split()

            tmp = []

            for j in range(len(element_split)):
                tmp.append(float(element_split[j]))

            matrix.append(tmp)

        print()

        # this if statement will compute determinant formula
        if n == 1:
            if len(matrix) != len(matrix[0]):
                print("Determinant doesn't exist!")
            else:
                printMatrix(matrix)
                print(f"\nDeterminant of the matrix -> {determinant(matrix):.2f} ")

        # this else if statement will compute inverse formula
        elif n == 2:
            if determinant(matrix) == 0:
                print("Inverse doesn't exist")
            else:
                print("Inverse of the matrix ->\n")
                newMatrix = inverse(matrix)
                printMatrix(newMatrix)
                print()

        time.sleep(3)
        while True:
            done = input("type done to reset: ")
            if done == "done":
                clear()
                break

# DETERMINANT
def determinant(matrix, pivot = 0):
    if len(matrix) == 1:
        return matrix[0][0]
    elif len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
    else:
        det = 0
        i = pivot
        for j in range(len(matrix)):
            cofactor = (-1)**(i+j) * matrix[i][j] * determinant(minor(matrix,i,j))
            det += cofactor # Sum all the cofactor by keeping it on det variable

    return det

def minor(matrix, row, column): # To find the smallest matrix (2x2) based on cofactor formula
    minorMatrix = []

    for i, rows in enumerate(matrix):
        temp = []
        for j, element in enumerate(rows):
            if i != row and j != column:
                temp.append(element)
        if len(temp) != 0:
            minorMatrix.append(temp)

    return minorMatrix



# INVERSE
def inverse(matrix):

    determinantMatrix = []

    for i, rows in enumerate(matrix):
        
        temp = []

        for j, element in enumerate(rows):
            temp.append(determinant(minor(matrix,i,j)))
        determinantMatrix.append(temp)

    # transposing the determinant matrix
    inverted = []

    for i in range(len(determinantMatrix[0])):
        col = []
        for cols in determinantMatrix:
            col.append(cols[i])
        inverted.append(col)

    det = determinant(matrix)

    for i, rows in enumerate(determinantMatrix):
        for j, element in enumerate(rows):
            inverted[i][j] = (-1)**(i + j) * element * (1.0 / det)

    return inverted



# PRINT MATRIX
def printMatrix(matrix):
    print("\n".join(["".join([("{:8.2f}".format(v)) for v in row]) for row in matrix]))



# OTHER FUNCTION
# Display for user to choose which one they want to calculate
def intro():
    print("---------------------------------")
    print("======= MATRIX CALCULATOR =======")
    print("---------------------------------\n")
    print("[1] Find the Determinant!")
    print("[2] Find the Inverse!")
    print("[0] EXIT\n")
    print("=================================\n")
    userCase = int(input("input -> "))
    
    return userCase

def clear():
    os.system('cls')



# Used to execute some code only if the file was run directly, and not imported
if __name__ == "__main__":
    main()