#1번

print(min(2, 3, 4))
print(max(2, -3, 4, 7, -5))
print(max(2, -3, min(4, 7), 5))
print('-------------')
#2번

print(min(max(3, 4), abs(-5)))
print(abs(min(4, 6, max(2, 8))))
print(round(max(5.572, 3.258), abs(-2)))
print('-------------')

"""
>>> help(round)
Help on built-in function round in module builtins:

round(number, ndigits=None)
    Round a number to a given precision in decimal digits.

    The return value is an integer if ndigits is omitted or None.  Otherwise
    the return value has the same type as the number.  ndigits may be negative.
"""

#3번

def f(x:int) :
    return(3 * x)

print(f(2))
print('-------------')

#4번

def g(a, b) :
    return(abs(a-b))

print(g(5, 6))
print('-------------')

#5번

def kilo_to_mile(x : int) :
    return(x/1.6)   # x = kilometer

print(kilo_to_mile(3))
print('-------------')

#6번

def pyeong(a, b, c) :
    return((a+b+c)/3)
"""
    if((a, b, c) <0):
        print('잘못된 점수입니다.')

    elif((a, b, c)>100):
        print('잘못된 점수입니다.')

    else:
        return((a+b+c)/3)
"""
print(pyeong(20, 80, 75))
print('-------------')


#7번

def score(a, b, c, d) :
    return(((a+b+c+d)-min(a,b,c,d))/3)

print(score(20, 45, 78, 65))
print('-------------')

#8번

def weeks_elapsed(day1, day2 : int) :
    return(round(abs(day1-day2)/7, 45))

print(weeks_elapsed(40, 60))
print('-------------')      #????????????

#8번-2

import math
def weeks_elapsed(day1, day2) :
    return(math.floor(abs(day1-day2)/7))

print(weeks_elapsed(40, 60))
print('-------------')  #인터넷을 통한 내림 함수의 사용

#9번, 10번

def square(num):
    return(num**2)

print(square(3))
