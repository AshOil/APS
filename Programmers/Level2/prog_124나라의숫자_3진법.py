def solution(number):
    result = ''
    while number:
        if number % 3 == 1:
            result = '1' + result
        elif number % 3 == 2:
            result = '2' + result
        else:
            result = '4' + result
        number = (number-1)//3
    return result