# 다음의 결과와 같이 사용자로부터 콤마(,)로 구분해 여러 원의 반지름을 입력 받아
# 이들에 대한 원의 둘레를 계산해 출력하는 프로그램을 작성하십시오.
import math

number = input()
result = number.split(", ")

r1 = [round(math.pi*float(i)*2.0,2) for i in result]

for i in r1:
    print("{0}".format(i),end=' ')
