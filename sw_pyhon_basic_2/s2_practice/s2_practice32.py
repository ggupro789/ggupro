# 다음과 같이 사용자가 입력한 문장에서 숫자와 문자를 구별해 각각의 개수를 출력하는 프로그램을 작성하십시오.
# hello world! 123

anum = input()
countA = 0
count1 = 0

result = list(anum)

for i in result:
    if(i.isalpha()==True):
        countA += 1
    elif(i.isalnum()==True):
        count1 += 1

print("LETTERS {0}".format(countA))
print("DIGITS {0}".format(count1))

