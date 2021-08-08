# ASCII 코드 값를 입력받아 문자를 확인하는 코드를 작성하십시오.

numberA = int(input())

def changeA(x):
    y=chr(x)
    print("ASCII {0} => {1}".format(x,y))


changeA(numberA)
