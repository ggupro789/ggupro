number = int(input())
x = 0 # x= 나머지
y = 0 # 2로 나눈 값 치환
rest = []

while True:
    going = int(number%2)
    y = int(number/2)
    if(y != 1): # 2로 나눴을 때 나눠 떨어지는지
        number = y
        rest.append(str(going))
    else:       # 2로 나눠떨어지면 값들 넣고 반복문 탈출
        rest.append(str(going))
        rest.append(str(y))
        break

result = ''.join(reversed(rest)) # 리스트 역순으로 문자열로 변환
print(result)