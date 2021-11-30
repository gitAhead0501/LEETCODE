"""
Convert any decimal number in Binary representation

"""

def decimalToBinary(number):
    if number >= 1:
        decimalToBinary(number // 2)
    print(number%2,end=" ")

# OR INBUILT FUNCTION

x = 4
bin(x)