# 다음 결과와 같이 문자열을 입력하면 짝수 인덱스를 가진 문자들을 출력하는 프로그램을 작성하십시오.

a = input()
result = list(a)

for i in range(len(result)):
    if(i%2 == 0 and i<len(result)):
        print("{0}".format(result[i]),end='')
    elif(i%2 == 0 and i == len(result)):
        print("{0}".format(result[i]))
