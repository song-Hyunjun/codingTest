import math
def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    num1 = numer1*denom2+numer2*denom1
    num2 = denom1*denom2 
    num3 = math.gcd(num1, num2)
    
    return [num1//num3,num2//num3]