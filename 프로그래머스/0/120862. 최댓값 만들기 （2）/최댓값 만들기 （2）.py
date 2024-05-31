def solution(numbers):
    numbers.sort()
    num1 = numbers[-1]
    num2 = numbers[-2]
    num3 = numbers[0]
    num4 = numbers[1]
    
    answer1 = num1*num2
    answer2 = num3*num4
    
    if answer1 > answer2:
        return answer1
    else:
        return answer2