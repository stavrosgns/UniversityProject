"""
This module is the implementation of the vigenere cipher.
"""

"""
@Author: Stavros Gkounis (it15178)
@Date : 26/10/17
@Project: Vigenere cipher
@Thesis: Classical cryptalgorithms, Cryptanalysis and Information Case Study (Network and Internet Applications Security)
"""

"""
|About Vigenere|:

|General Information|:
The Vigenère cipher is a method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword.
With simple word is a polyalphabetic substitution.

|Encryption - Decryption|:
To encrypt a message using the vigenere cipher, we use a table which is well-known in cryptography as tabula recta. The Format of this table is shown here:

Plain Text letters
|
|
V
        00  01  02  03  04  05  06  07  08  09  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25
        A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z  <---- Key letters
00 A    A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z
01 B    B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A
02 C    C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B
03 D    D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C
04 E    E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D
05 F    F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E
06 G    G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F
07 H    H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G
08 I    I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H
09 J    J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I
10 K    K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J
11 L    L   M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K
12 M    M   N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L
13 N    N   O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M
14 O    O   P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N
15 P    P   Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O
16 Q    Q   R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P
17 R    R   S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q
18 S    S   T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R
19 T    T   U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S
20 U    U   V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T
21 V    V   W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U
22 W    W   X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V
23 X    X   Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W
24 Y    Y   Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X
25 Z    Z   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O   P   Q   R   S   T   U   V   W   X   Y

1) Practically the encryption letter is using the table with the following order. (Key Letter, Plain Text Letter) = Cipher Text Letter.
Where the (Key Letter, Plain Text Letter is) is the coordinates of the Cipher Text letter in the table.

2) In mathematical formulation, what we are doing is the following:
    Ci = (Mi + Ki) mod 26   |where Ki is the key that is used to encrypt the message
    Mi = (Ci - Ki) mod 26   |and Mi is the plaintext that we acquire after decryption.

|Cryptanalysis|:
The Cryptanalysis of the Vigenere cipher based on the kasiski's hypothesis or kasiski's test, that we can take advatange of the fact that repeated words may,
probably (Using Probabilities), sometimes be encrypted using the same key letters, leading to the repeated groups in ciphertext.
For example:

Plain Text : cryptoisshortforcryptography
Key        : abcdabcdabcdabcdabcdabcdabcd
Cipher Text: CSASTPkvsiqutgquCSASTPiuswjb  # The capital letter is used to highlight the repeated group.
"""

englishAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def Ascii2Zset(plaintext):
    if(plaintext.isupper()):
        return [ord(x)-65 for x in plaintext]
    return [ord(x)-97 for x in plaintext]

def Zset2Ascii(ciphertext):
    return "".join([chr(x+65) for x in ciphertext])

def tabulaRecta(message,key):
    #Begin of precomputed variables
    plainText = Ascii2Zset(message)
    messageLength = len(plainText)
    keyLength = len(key)
    key_is_string = isinstance(key,str)
    #End of precomputed variables

    if(key_is_string):
        keyList = Ascii2Zset(key)
        if((keyLength == messageLength) or (keyLength > messageLength)):
            return [((keyList[x] + plainText[x]) % 26) for x in range(len(plainText))]
        elif(keyLength < messageLength):
            return [((keyList[x % keyLength] + plainText[x]) % 26) for x in range(len(plainText))]


def plaintextInAscii(ciphertext, key):
    ciphertextList = Ascii2Zset(ciphertext)
    keyAscii = Ascii2Zset(key)
 
    keyLength = len(keyAscii)
    cipherLength = len(ciphertext)
    return ([((ciphertextList[x] - keyAscii[x % keyLength]) % 26) for x in range(len(ciphertext))])


def decryption(ciphertext,key):
    ciphertextList = plaintextInAscii(ciphertext,key)
    #print(ciphertextList)
    cipherT = Zset2Ascii(ciphertextList)
    return "".join(cipherT)

def mappingSortedOrder(key):
    if(isinstance(key,str)):
        sortedOrder = [x+1 for x in range(len(key))]
        return "".join([chr(x+65) for x in sortedOrder]), "".join(sorted(list(key)))


def sortedTabulaRecta(message,key):
    #Begin of precomputed variables
    plainText = Ascii2Zset(message)
    messageLength = len(plainText)

    keyLength = len(key)
    asciiKey = Ascii2Zset(key)

    mapping, sortedList = mappingSortedOrder(key)
    #End of precomputed variables

    #CEMOPRTU    --> COMPUTER
    #BCDEFGHI    --> BEDFIHCG

    aux = [mapping[sortedList.index(key[x])] for x in range(len(key))]
    newKey = Ascii2Zset("".join(aux))

    return [((newKey[x % len(newKey)] + plainText[x]) % 26) for x in range(len(plainText))]


def ciphertextInAscii(ciphertext,key):
    ciphertextList = Ascii2Zset(ciphertext)
    keyAscii = Ascii2Zset(key)

    keyLength = len(keyAscii)
    cipherLength =  len(ciphertextList)

    mapping, sortedList = mappingSortedOrder(key)

    aux = [mapping[sortedList.index(key[x])] for x in range(len(key))]
    newKey = Ascii2Zset("".join(aux))

    return [((ciphertextList[x] - newKey[x % len(newKey)]) % 26) for x in range(len(ciphertext))]

def sortedDecryption(ciphertext, key):
    ciphertextList = ciphertextInAscii(ciphertext,key)
    cipherT = Zset2Ascii(ciphertextList)
    return "".join(cipherT)


def encryption(message, key):
    cipherList = tabulaRecta(message,key)
    return Zset2Ascii(cipherList)

def sortedEncryption(message,key):
    cipherList = sortedTabulaRecta(message,key)
    return Zset2Ascii(cipherList)

def BruteForceVigenere(fileN):
    ciphertext1 = 'VIEOEGMOCIGOHHJGBALOTMRJBHUMPXRJKQAMMBZAZKLMROROMQRAAUMNFWUGKXRNGKKUCTXKXJLXGNXAFWQCHLBIAJLJVVQSHLVBVSXQZBUIKSGBBUEUELFZNXPKNXXZLTYEMBVIIGBFRJYKUIFSFGGXUWAUMZFZTKMNYIGNXVZOTKLNSWBQBMZVGNXCEBRXGYK'
    
    inF = open(fileN)
    textList = inF.read()
    possibleKeys = textList.split('\n')
    
    for i in possibleKeys:
        print("Key: {}     PlainText: {}".format(i,decryption(ciphertext1,i)))
        
    inF.close()


if(__name__ == "__main__"):
    print(encryption("GKOUNISS","SORV"))
    print(decryption("YYFPFWJN","SORV"))
    print('\n')
    
    print(sortedEncryption("GKOUNISS","SORV"))
    print(sortedDecryption("JLQYQJUW", "SORV"))
    print('\n')

    BruteForceVigenere('Alist.txt')
    print('\n')

else:
    print("The module is imported successfully!")
