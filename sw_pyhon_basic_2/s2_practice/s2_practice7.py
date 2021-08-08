# 다음의 결과와 같이 정수를 입력하면 약수를 리스트에 추가해 출력하는 코드를 작성하십시오.

x = int(input())

result = [i for i in range(1,x+1) if(x%i == 0)]
print(result)
