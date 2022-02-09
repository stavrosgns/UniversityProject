"""
|Code Description|:
This is a python script code that take a multi-dimensional matrix and creates a dictionary SMatrix and its keys
are the position of non-zero elements of the Matrix and its values are the non-zero elements.
"""

"""
|DETAILS ABOUT THE PROJECT|:

@Author: Stavros Gkounis
@Date: 23/08/17
@Project: Calculate Sparse Matrix
@Version: v1.0
"""

Matrix = [[ 3,  0, -2, 11],
          [ 0,  9,  0,  0], #  Just for Debugging
          [ 0,  7,  0,  0],
          [ 0,  0,  0, -5]]

Array = [[ 0, -4,  0,  0,  0],
         [-2,  0,  1,  0,  0],
         [ 0,  0,  1,  0,  0], #  Just for Debugging
         [ 0,  1,  0,  0, -5],
         [ 0,  0,  0, -9,  0]]


def askUser():
    """
    This function ask from the user the dimensions of the array and then ask the user to give integers for each row.
    """
    IMatrix = [] #  This matrix will be created with the user's help
    row = int(input("How many Constrains ? ")) # input returns the input as a string.
    col = int(input("How many Variables ? ")) # ---------------- || ----------------

    for i in range(0,row): # for each row
        userValues = [] # auxilary list
        print("Start inserting in Row {}: \n".format(i+1)) #Values for what row ?
        for j in range(0,col): # Give values as many as the variables
            userValues.append(int(input("Give a element to append in the row: "))) # Give the values
        print("End inserting in Row {} \n".format(i+1)) # OK, we finished with i row
        IMatrix.append(userValues) # Insert the row to the IMatrix.
    #print(IMatrix) #Just for debugging
    Sparse_Matrix(IMatrix) # Calling the Sparse_Matrix function with IMatrix as input.

def Sparse_Matrix(Matrix):
    """
    This function calculates the Sparse Matrix.
    """
    SMatrix = {} # Empty Dictionary

    row = 0
    for nestedList in Matrix:
        col = 0
        for num in nestedList:
            if(num != 0):
                SMatrix.setdefault((row, col), num) #Check the dictionary. If you don't find (row,col) in it then add as key the (row, col) and as value the num {Alternative: SMatrix[(row,col)]] = num}
            col += 1
        row += 1
    print("SMatrix {}".format(SMatrix)) # Return the Dictionary. Not sorted.

def Return_Sparse_Matrix(Matrix):
    """
    This function calulates the Sparse Matrix and returns the SMatrix dictionary instead of printing it.
    """
    SMatrix = {}

    row = 0
    for nestedList in Matrix:
        col = 0
        for num in nestedList:
            if(num != 0):
                SMatrix.setdefault((row, col), num)
            col += 1
        row += 1
    return SMatrix
