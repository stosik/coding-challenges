# https://en.wikipedia.org/wiki/Binomial_coefficient#Multiplicative_formula

LIMIT = 1000000000

def fulfil_initial_assumption(N, K):
    return not 0 <= K <= N

def is_out_of_range(bin_cof):
    return bin_cof > LIMIT

def binomial_coefficient(N, K):
    if fulfil_initial_assumption(N, K) :
        return -1
    
    binomial_coefficient = 1
    
    for i in range(1, N)):
        binomial_coefficient = binomial_coefficient + 1 - i
        binomial_coefficient /= i
        if is_out_of_range(binomial_coefficient):
            return -1
        N -= 1
    
    return int(binomial_coefficient)
    
def solution(N, K):
    return binomial_coefficient(N, K)


print(solution(5,3))
print(solution(40, 20))