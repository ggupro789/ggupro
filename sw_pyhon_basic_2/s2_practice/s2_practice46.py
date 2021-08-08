# # name 프로퍼티를 가진 Student를 부모 클래스로 major 프로퍼티를 가진
# GraduateStudent 자식 클래스를 정의하고 이 클래스의 객체를
# 다음과 같이 문자열로 출력하는 코드를 작성하십시오.

from typing import SupportsAbs, overload


class Student:
  def __init__(self,name):
      self.__name = name
  

  def print_name(self):
      print("이름: {0}".format(self.__name))
  
  @property
  def set_name(self,name):
      self.__name == name

class GraduateStudent(Student):
    def __init__(self, name, major):
        Student.__init__(self,name)
        self.__major = major
    
    def print_other_name(self):
        print("이름: {0}".format(self.__name),end=', ')
        print("전공: {0}".format(self.__major))

kim = GraduateStudent("홍길동","컴퓨터")
kim.print_name()


