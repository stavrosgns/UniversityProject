"""
This module contains two functions.
The purpose of this module is to calculate the last index of a object which appears multiple times in an list.
Actually, fills the gap of the .index list attribute which returns the index of the first object and discards
the other indexes.
"""

"""
@Author : Stavros Gkounis
@Date : 5/09/17
"""

index = {} #  Global Empty dictionary
def getLastIndex(ls,elmt):
    """
    This function is the main function of the module, and returns the last index of a give object in a list.
    """
    if(ls.count(elmt) > 1): # If the elmt appears more than 1 times.
        indx = [] # auxilary list. It keeps all the indexes of the element elmt
        for i in range(0,len(ls)): # from the first index through the last index of the list.
            if(ls[i] == elmt): # if the element of the ith position is the elmt
                indx.append(i) # appeand to the list indx the index of its position.
        index[elmt] = tuple(indx) #  Transform the list to tuple and add it as value to the dictionary's key.
        del indx # we delete the useless, in this phase, auxilary list.
    else:
        index[elmt] = ls.index(elmt) # If the elmt appears only one time, then add this unique index as a value to dictionary's key.

    if(isinstance(index[elmt],tuple)): #  If the dictionary's value is tuple, then transform it to a list and return the last index
        l = list(index[elmt])
        return l[len(l)-1]
    return index[elmt] # otherwise, return the unique index.

def getAllIndexes(ls,elmt):
    """
    This function returns all the indexes as a list that the element elmt is appeared in a list.
    """
    indexes = []
    for i in range(0,len(ls)):
        if(ls[i] == elmt):
            indexes.append(i)
    return indexes
