#  다음과 같이 2차원 배열 구조를 만들기 위한 행, 열 정보를 콤마(,)로 구분해 입력하고,
# 이 리스트 객체의 항목의 값은 행과 열의 인덱스 곱으로 초기화해 출력하는 프로그램을 작성하십시오.

number = input()
result = number.split(", ")
re = []

for i in range(int(result[0])):
    get = []
    for j in range(int(result[1])):
       get.append(i*j)

    re.append(get)

print (re) 