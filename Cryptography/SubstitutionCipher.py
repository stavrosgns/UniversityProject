"""
This Python module implements the substitution cipher (cryptalgorithm).
"""

"""
@Author : Stavros Gkounis
@Date : 10/11/17
@Project : Substitution Cipher implementation.
"""

"""
Basic Notion:

Set A:                            Set B (Permutation of Set A) (One of the 4x10^26 possible permutations):

A (01)     <---------->           Z (26)
B (02)     <---------->           A (01)
C (03)     <---------->           Y (25)
D (04)     <---------->           B (02)
E (05)     <---------->           X (24)
F (06)     <---------->           C (03)
G (07)     <---------->           W (23)
H (08)     <---------->           D (04)
I (09)     <---------->           V (22)
J (10)     <---------->           E (05)
K (11)     <---------->           U (21)
L (12)     <---------->           F (06)
M (13)     <---------->           T (20)
N (14)     <---------->           G (07)
O (15)     <---------->           S (19)
P (16)     <---------->           H (08)
Q (17)     <---------->           R (18)
R (18)     <---------->           I (09)
S (19)     <---------->           Q (17)
T (20)     <---------->           J (10)
U (21)     <---------->           P (16)
V (22)     <---------->           K (11)
W (23)     <---------->           O (15)
X (24)     <---------->           L (12)
Y (25)     <---------->           N (14)
Z (26)     <---------->           M (13)

The inverse Permutation of Set B (which is a swap of each letter and the index of the letter) is:
 A  B  C  D  E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V  W  X  Y  Z
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 25, 23, 21, 19, 17, 15, 13, 11, 9, 7, 5, 3, 1]

the inverse permutation practically tells us that if you see the letter A in ciphertext then is B in plaintext,
                                                  if you see the letter B in ciphertext then is D in plaintext,
                                                  if you see the letter C in ciphertext then is H in plaintext,
                                                                               .
                                                                               .
                                                                               .
                                                                               .
                                                  if you see the letter Y in ciphertext then is C in plaintext,
                                                  if you see the letter Z in ciphertext then is A in plaintext.
"""
alphab = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
permut = 'ZAYBXCWDVEUFTGSHRIQJPKOLNM'
perm = [ord(x)-64 for x in permut]

def Ascii2Zset(message):
    """
    This function takes a plaintext and maps every letter to Z(26) set : A <--> 0, B <--> 1, C <--> 2, ... , Z <--> 25
    """
    if(message.isupper()):
        return [ord(x)-65 for x in message] #  ord('A') --> 65
    return [ord(x)-97 for x in message] #  ord('a') --> 97


def Zset2Ascii(MsgList):
    """
    This function maps the 0 <--> A, 1 <--> B, 2 <--> C, ..., 25 <--> Z
    """
    return "".join([chr(x+65) for x in MsgList])


def SubstitutionCipher(plaintext, permutation):
    """
    This funtion is the implementation of the cryptalgorithm Substitution Cipher. Give a plaintext and permutation encrypts the message.
    """
    plaintextList = Ascii2Zset(plaintext)
    substitution = [permutation[plaintextList[i]]-1 for i in range(len(plaintextList))]
    return Zset2Ascii(substitution)


def InversePermutation(permutation):
    """
    This function calculates the Inverse Permutation of a given permutation. More details look the Basic Notion Documentation.
    (It's not mathematical correct.)
    """
    InversePermut = []
    alphabInASCII = [ord(x) -64 for x in alphab]

    for i in range(1,27):
        InversePermut.append(alphabInASCII[permutation.index(i)])
    return InversePermut

def DSubstitutionCipher(ciphertext,permutation):
    """
    This function, given a ciphertext and permutation, deciphers the message.
    """
    ciphertextList = Ascii2Zset(ciphertext)
    invperm = InversePermutation(permutation)
    reverseSubstitution = [invperm[ciphertextList[i]]-1 for i in range(len(ciphertextList))]
    return Zset2Ascii(reverseSubstitution)


if __name__ == "__main__":
    print("- {}".format(SubstitutionCipher("MEETME",perm)))
    print("- The above message doesn't make any sense. DECIPHER IT.\n- OK, there you are.")
    print("- {}".format(DSubstitutionCipher("TXXJTX",perm)))
    print("- Much better.")
else:
    print("The SubstitutionCipher python module is imported successfully.")
