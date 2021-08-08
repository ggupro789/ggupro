#  콤마(,)로 구분해 숫자를 입력하고, 입력된 숫자 중 홀수를 콤마(,)로 구분해 출력하는
# 리스트 내포 기능을 이용한 프로그램을 작성하십시오.


number = input()
result = number.split(", ")
result1 = [int(i) for i in result if(int(i)%2 != 0)]

for i in range(len(result1)):
    if i == len(result1) -1 :
        print(result1[i])
    else :
        print(result1[i],end =', ')