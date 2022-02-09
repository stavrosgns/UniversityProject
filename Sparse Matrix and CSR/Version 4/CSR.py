"""
|Code Description|:
This python script take a multi-dimensional matrix and calculate the Compressed Sparse Row (CSR).
"""

"""
|DETAILS ABOUT THE PROJECT|:
@Author: Stavros Gkounis
@Date: 5/09/17
@Project:Compressed_Sparse_Row
@Version: v3.0
@Modified Date: 6/09/17
"""

"""
|ABOUT VERSION 2|:
The version 2 add the interactive element, the matrix to be filled by the user,
which was missing from the version 1.
"""

"""
|ABOUT VERSION 3|:
The version 3 fixes some bugs about the calculation of the JA and IA lists.
"""

import Index #My Module
import SMatrix #My Module

Matrix = [[ 3,  0, -2, 11],
          [ 0,  9,  0,  0],   #  For Debugging Purposes
          [ 0,  7,  0,  0],
          [ 0,  0,  0, -5]]

Array = [[ 0, -4,  0,  0,  0],
         [-2,  0,  1,  0,  0],
         [ 0,  0,  1,  0,  0], #  For Debugging Purposes
         [ 0,  1,  0,  0, -5],
         [ 0,  0,  0, -9,  0]]

Pinakas = [[ 1,   0,  0,  4,  0],
           [ 0,   0,  0,  0,  0], #  For Debugging Purposes
           [ 3,   0,  0,  0,  5], 
           [ 0,   0,  0,  0,  0], #  Zero Row
           [ 0,   2,  0,  0,  9]]



def askUser():
    """
    This function ask from the user the dimensions of the array and then ask the user to give integers for each row.
    """
    IMatrix=[] # IMatrix will be created with the user's help.
    row = int(input("How many Constrains ? ")) # input returns the input as a string.
    col = int(input("How many Variables ? ")) # ---------------- || ----------------

    for i in range(0,row):  # for each row
        userValues = [] # auxilary list
        print("Start inserting in Row {}: \n".format(i+1)) #Values for what row ?
        for j in range(0,col): # Give values as many as the variables
            userValues.append(int(input("Give a element to append in the row: "))) # Give the values
        print("End inserting in Row {} \n".format(i+1)) # OK, we finished with i row
        IMatrix.append(userValues) # Insert the row to the IMatrix.

    Compressed_Sparse_Row(IMatrix) # Calling the Compressed_Sparse_Row function with IMatrix as input.


def NumberOfVariables(Matrix):
    """
    This function returns the number of the variables and assumes that the length of the first row
    is the same as the other one.

    There's no exception handler (!)
    """
    return len(Matrix[0])

def Compressed_Sparse_Row(Matrix):
    """
    This function calculate the Compressed Sparse Row of a given Matrix.
    """

    anz = []
    ja = []
    ia = []
    ZRow = [] # We keep the indexes of the zero rows

    SparseM = SMatrix.Return_Sparse_Matrix(Matrix) # SparseM contains the dictionary which is returned by the Return_Sparse_Matrix function.
    sortedSparseM = sorted(SparseM) #  sorted(SparseM) returns only the keys of the dictionary in sorted order.

    ZR = [0 for i in range(0,NumberOfVariables(Matrix))] #  Creates a list of zero as many as the number of variables that the problem contains, using list comprehension.
    ZRow = Index.getAllIndexes(Matrix,ZR) # ZRow contains all the indexes of rows that all elements are zero.

    for row in Matrix:
        Lock = 1 # This is a lock boolean variable, that doesn't allow other element in the same row except from the first one to be appended in the IA list
        for elmt in row:
            if(elmt != 0):
                anz.append(elmt)
                if(Lock == 1):
                    ia.append(Index.getLastIndex(anz,elmt)+ 1)
                    Lock = 0

    """
    This loop iterates the list of tuples, which is the coordinates of the non-zero elements in the table.
    We take only the column index, we increase it by one to be human readable and we add it to the JA list.
    """
    for key in sortedSparseM:
        ja.append(key[1] + 1)

    """
    | Explanation of the expression "not (not ZRow)" |:
    The following loop is the COPY BACK TECHNIQUE, if the matrix has zero rows.

    If the ZRow is empty the expression (not ZRow) returns "True". Is a easy way to check if a list is empty.
    So, the expression "not (not ZRow)" means that if the ZRow is not empty then execute the for-loop.
    """

    if(not (not ZRow)):
        for i in ZRow:
            ia.insert(i,ia[i])
    ia.append(len(anz) +1)

    print("ANZ : {}\nJA : {}\nIA :{}".format(anz, ja, ia)) # We print the result.
