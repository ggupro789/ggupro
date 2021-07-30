# 두 개의 문자열 str1과 str2가 주어진다. 문자열 str2 안에 str1과 일치하는 부분이 있는지 찾는 프로그램을 만드시오.

test_case= int(input())

def find(p,char):    #문자열 비교 해서 str1과 일차하는 여부에 따라서 이동할 길이 
    for i in range(len(p)-2,-1,-1):
        if p[i] == char:
            return len(p)-i-1
    return len(p)

def find_pattern(x:str,y:str):
    p = len(x)
    t = len (y)
    i = 0

    while i <= t-p:
        j  = p-1  # 뒤에서 부터 연산하기 위함

        while j >= 0:
            if(p[j] != t[i+t-1]): # 패턴의 맨 뒷글자와 그 글자 길이만큼 더해서 비교
                move = find(x,t[i+p-1])
                break
            j=j-1
            if j == -1:
                return True
            else:
                i += move
    return False
    
for i in range(test_case):
    str1 = input()
    str2 = input()

    