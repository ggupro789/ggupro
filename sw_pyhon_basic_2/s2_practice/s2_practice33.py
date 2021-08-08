# 다음과 같이 사용자가 입력한 문장에서 대소문를 구별해 각각의 갯수를 출력하는 프로그램을 작성하십시오.

anum = input()
countA = 0
counta = 0

result = list(anum)

for i in result:
    if(i.isalpha() == True):
        if(i == i.upper()):
            countA += 1
        elif(i == i.lower()):
            counta += 1

print("UPPER CASE {0}".format(countA))
print("LOWER CASE {0}".format(counta))



