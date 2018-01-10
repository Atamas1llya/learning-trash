import sys;

def decimal2binary(decimal):
    bits = ['0'];
    rest = decimal;

    while rest > 0:


        if rest == 1:
            bits[len(bits) - 1] = '1';
            rest = 0;

        i = 1;
        while 2**i <= decimal:
            if len(bits) <= i:
                for z in range(len(bits), i + 1):
                    bits.append('0');

            if decimal < 2**(i + 1):
                bits[i] = '1';
                rest = decimal - 2**i;

                x = i;


            i += 1

        y = len(bits);
        while y >= 0:
            if 2**y == decimal:
                bits[y] = '1';
            y -= 1;

        decimal = rest;


    return ''.join(bits[::-1])

print(decimal2binary(int(sys.argv[1])))
