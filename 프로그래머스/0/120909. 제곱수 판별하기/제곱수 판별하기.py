import math

def solution(n):
    # n의 제곱근 구하기 
    sqrt_n = math.isqrt(n)
    # 제곱근 * 제곱근이 제곱수와 같다면 1 아니면 2
    if sqrt_n * sqrt_n == n:
        return 1
    else:
        return 2