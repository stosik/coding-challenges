# https://en.wikipedia.org/wiki/Negative_base
import math

def get_bits_from_dec(decimal):
    if decimal == 0:
        arr = [0]
    else:
        arr = []
        while decimal != 0:
            decimal, remainder = divmod(decimal, -2)
            if remainder < 0:
                decimal, remainder = decimal + 1, remainder + 2
            arr.append(remainder)
        return arr

def get_decimal_from_bits(bits):
    result = 0
    
    for index, bit in enumerate(bits):
        result += bit * int(math.pow(-2, index))
        
    return result

def solution(A):
    if not A:
        return []
    
    decimal = math.ceil(get_decimal_from_bits(A) / 2)
    print(decimal)
    print(get_bits_from_dec(decimal))

solution([1, 0, 0, 1, 1]) # 5
solution([1, 0, 0, 1, 1, 1]) # -23 => -11 => [1, 0, 1, 0, 1, 1]
solution([1, 0, 0, 0, 0, 0, 1]) # 65 => 33 => [1, 0, 0, 0, 0, 1, 1]