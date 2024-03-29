from a09_caesar_cipher import *
import sys

def testit(did_pass):
    """  Prints the result of a test.  """
    linenum = sys._getframe(1).f_lineno   # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def CaesarCipher_test_suite():
    """
    A test suite for testing the encrypt and decrypt methods of the class

    NOTE:
    Typically, a test suite for a Class would be written into a second class entirely.
    However, to keep the complexity low, I chose to incorporate the test suite in a familiar way.
    In the future, we will explore how to properly write a test suite as a separate class.
    """

    # tests encrypting a normal string
    caesar = CaesarCipher()
    caesar.key = 3
    caesar.message = "A test string"

    testit(caesar.encrypt() == "D WHVW VWULQJ")

    # tests encrypting a string with punctuation
    caesar.key = 13
    caesar.message = "It's a so-so kind of day!"

    testit(caesar.encrypt() == "VG'F N FB-FB XVAQ BS QNL!")

    # tests decrypting a normal string
    caesar.message = "A test string"
    caesar.key = 3
    caesar.cipher = "D WHVW VWULQJ"
    caesar.crypt_type = "decrypt"

    testit(caesar.decrypt() == "A TEST STRING")

    # tests decrypting a string with punctuation
    caesar.message = "It's a so-so kind of day!"
    caesar.key = 6
    caesar.cipher = "OZ'Y G YU-YU QOTJ UL JGE!"

    testit(caesar.decrypt() == "IT'S A SO-SO KIND OF DAY!")

    caesar.cipher = "H"
    caesar.key = 14
    testit(caesar.decrypt()=="T")

    caesar.cipher = "E"
    caesar.key = 6
    testit(caesar.decrypt() == "Y")


    caesar.cipher="FGCT DTWVWU,"
    caesar.key =2
    testit(caesar.decrypt()=="DEAR BRUTUS,")

    caesar.message="DEAR BRUTUS,"
    caesar.key=2
    testit(caesar.encrypt()=="FGCT DTWVWU,")

    caesar.message="1234567890-=[][]"
    caesar.cipher = "1234567890-=[][]"
    testit(caesar.decrypt()=="1234567890-=[][]")
    testit(caesar.encrypt() == "1234567890-=[][]")

    caesar.message = "?>?>"
    caesar.cipher = "?>?>"
    caesar.key = 6
    testit(caesar.decrypt() == "?>?>")
    testit(caesar.encrypt() == "?>?>")

    caesar.message = "FGCT DTWVWU,"
    caesar.key = -2
    testit(caesar.encrypt() == "DEAR BRUTUS,")

    caesar.cipher = "FGCT DTWVWU,"
    caesar.key = -2
    testit(caesar.encrypt() == "DEAR BRUTUS,")

    # what other tests should you add?
    #Tests containing other symbols than just several of the 26 alphabets
    #Tests with caesar.key <0
CaesarCipher_test_suite()
