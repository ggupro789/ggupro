# 인자로 전달된 두 개의 문자열 중 길이가 더 긴 문자열을 출력하는 함수를 정의하고
 

z = input()

def longer(x):
    y = x.split(',')
    y1 = []
    for i in y:
        y1.append(i.strip())
    o = []
    j = 0
    for i in y1:
        o.append(len(i))
    
    print(y1[o.index(max(o))])


longer(z)