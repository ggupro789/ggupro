# Shape를 부모 클래스로 Square 자식 클래스를 정의하는 코드를 작성하십시오.
# Square 클래스는 length 필드를 가지며, 0을 반환하는 Shape 클래스의 area 메서드를
# length * length 값을 반환하는 메서드로 오버라이딩합니다.

class Shape:
    def __init__(self):
        pass


    def area(self):
        return 0

class Square(Shape):
    length = 0
    def __init__(self):
        pass

    
    def area(self,dd):
        length = dd
        return length * length

what = Square()
print("정사각형의 면적: {0}".format(what.area(3)))