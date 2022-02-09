"""
This module executes the Functions Compressed_Sparse_Row and Sparse_Matrix, without the user to execute pre-code commands.
"""

"""
@Author : Stavros Gkounis
@Date : 5/09/17
@Last Modifed: 10/09/17
"""

def CompressedSparseRow():
    """
    Executes the Compressed_Sparse_Row function which is located to the CSR module.
    """
    import CSR

    CSR.askUser()

def SparseMatrix():
    """
    Executes the Sparse_Matrix function which is located to the SMatrix module.
    """
    import SMatrix

    SMatrix.askUser()

if __name__ == "__main__":
    print("Which algorithm do you prefer ?\n")
    ans = int(input("Type 1 for Sparse Matrix or\nType 2 for Compressed Sparse Row :"))
    if(ans == 1):
        SparseMatrix()
    elif(ans == 2):
        CompressedSparseRow()
    else:
        print("The available options is '1 or 2'. Try again")
else:
    print("The file Interactive.py is imported as a module.\nYou can use the function using the form : moduleName.Function()\n")
