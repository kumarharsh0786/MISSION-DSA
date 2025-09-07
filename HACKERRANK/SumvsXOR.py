def sumXor(n):
    if n == 0:
        return 1
    else:
        zero_bits = bin(n)[2:].count('0')  
        return 2 ** zero_bits
