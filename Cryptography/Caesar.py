"""
Caesar python Module is the implemation of the caesar cipher (cryptalgorithm).
"""

"""
@Author : Stavros Gkounis
@Date : 10/11/17
@Project : Caesar Cipher implementation.
"""

def Ascii2Zset(message):
    """
    This function takes a plaintext and maps every letter to Z(26) set : A <--> 0, B <--> 1, C <--> 2, ... , Z <--> 25
    """
    if(message.isupper()):
        return [ord(x)-65 for x in message] #  ord('A') --> 65
    return [ord(x)-97 for x in message] #  ord('a') --> 97

def Shift(Z,key):
    """
    This function takes the list of characters after mapping and shifts the letter as many times as the value of key variable.
    """
    return [(x+key) % 26 for x in Z]

def RShift(Z,key):
    """
    Same function of the Shift, just in Reverse order.
    """
    return [(x-key) % 26 for x in Z]

def Zset2Ascii(MsgList):
    """
    This function maps the 0 <--> A, 1 <--> B, 2 <--> C, ..., 25 <--> Z
    """
    return "".join([chr(x+65) for x in MsgList])

def Caesar(plaintext, key):
    """
    This fuction takes a plaintext, a key and encrypts the plaintext using the Caesar's cipher.
    """
    Zplaintext = Ascii2Zset(plaintext)
    cipherMsgList = Shift(Zplaintext, key)
    return Zset2Ascii(cipherMsgList)

def DCaesar(ciphertext,key):
    """
    This function takes a ciphertext, a key and decrypts the ciphertext using the Caesar's ciphertext
    """
    CipherMsgList = Ascii2Zset(ciphertext)
    plaintextList = RShift(CipherMsgList,key)
    return Zset2Ascii(plaintextList)

def BruteForceCaesar(ciphertext):
    """
    This function brute force all the possible keys to find the plaintext given a ciphertext.
    """
    for key in range(26):
        print("{}: {}".format(key, DCaesar(ciphertext,key)))

def BruteForceCaesarValidate(ciphertext,plaintext):
    """
    This function has the same functionality of the BruteForceCaesar function, but the procedure stops when the plaintext is found.
    """
    for key in range(26):
        possiblePlaintext = DCaesar(ciphertext,key)
        print("{} : {}".format(key, possiblePlaintext))
        if(possiblePlaintext == plaintext):
            break



if __name__ == "__main__":
    print(Caesar("hello",3))
    print(DCaesar("KHOOR",3))
    print("Brute Force be with you:\n") #  Star Wars pun.
    BruteForceCaesar("KHOOR")
    print("\n")
    BruteForceCaesarValidate("KHOOR","HELLO")
else:
    print("You have successfully imported the caesar module")
