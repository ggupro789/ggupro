# 다음의 결과와 같이 국어, 영어, 수학 점수를 입력받아 합계를 구하는 객체지향 코드를 작성하십시오.
# 이 때 학생 클래스의 객체는 객체 생성 시 국어, 영어, 수학 점수를 저장하며, 총점을 구하는 메서드를 제공합니다.

class korea:
    def __init__(self,x,y,z):
        self.__x = x
        self.__y = y
        self.__z = z

    def __del__(self):
        print("객체 소멸됨")

    def sum(self):
        return self.__x + self.__y + self.__z


score = input()
scores1 = score.split(', ')
scores = []
for i in scores1:
    scores.append(int(i))

student = korea(scores[0],scores[1],scores[2])
print("국어, 영어, 수학의 총점: %d"%(student.sum()))