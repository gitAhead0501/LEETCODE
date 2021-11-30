"""
Convert any decimal to representation of any base 2,3,4 etc

"""

def decimalToBinary(number,base):
    if number >= 1:
        decimalToBinary(number // base)
    print(number%base,end=" ")