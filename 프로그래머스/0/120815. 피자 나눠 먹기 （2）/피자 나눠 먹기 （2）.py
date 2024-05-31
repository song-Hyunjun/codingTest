import math

def solution(n):   
    # math.gcd() : 최대공약수 계산(둘 이상의 정수의 공약수 중 가장 큰 값)
    # ex) gcd(8,12)의 최대공약수는 4
    
    # math.lcm() : 최소공배수 계산(둘 이상의 정수의 배수중 가장 작은 값)
    # lcm 함수는 현재 파이썬 3.9 이상부터 지원 
    # ex) lcm(6,4)의 최소공배수는 12
    
    lcm = (6*n) // math.gcd(6,n)
        
    return lcm//6