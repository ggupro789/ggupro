# 반지름 정보를 갖고, 원의 면적을 계산하는 메서드를 갖는 Circle 클래스를 정의하고,
# 생성한 객체의 원의 면적을 출력하는 프로그램을 작성하십시오.
import math

class circle:
    def __init__(self,r):
        self.__r = r
    
    @property
    def good(self):
        return math.pi*(self.__r**2)
    

one1 = circle(2)
print("{0:.2f}".format(one1.good))
