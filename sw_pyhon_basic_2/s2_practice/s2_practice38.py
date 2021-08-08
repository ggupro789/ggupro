# 다음과 같이 문장을 구성하는 단어를 역순으로 출력하는 프로그램을 작성하십시오.

alpha = input()
result = list(reversed(alpha.split(' ')))

for i in range(len(result)):
    if(i<len(result)-1):
        print("{0}".format(result[i]),end=' ')
    else:
        print("{0}".format(result[i]))
