import sys;

def binary2decimal(binary):
    binary = list(binary)[::-1];
    decimal = 0;

    for index, bit in enumerate(binary):
        if int(bit):
            decimal += 2**index;

    return decimal;

print(binary2decimal(sys.argv[1]));
