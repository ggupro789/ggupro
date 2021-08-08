# 가로, 세로 정보을 갖고, 사각형의 면적을 계산하는 메서드를 갖는 Rectangle 클래스를 정의하고,
# 생성한 객체의 사각형의 면적을 출력하는 프로그램을 작성하십시오.

class Rectangle:
    def __init__(self,garo,sero):
        self.__garo = garo
        self.__sero = sero

    @property
    def good(self):
        return self.__garo * self.__sero

R = Rectangle(10,2)
print("사각형의 면적: {0}".format(R.good))
