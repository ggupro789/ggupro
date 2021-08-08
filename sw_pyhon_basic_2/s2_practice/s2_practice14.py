# 콤마(,)로 구분된 정수 값을 입력받아 리스트와 튜플 객체를 생성하는 코드를 작성하십시오.
# 12, 34, 56, 78

number = input()
result = number.split(", ")

r1 = [int(i) for i in result ]
r2 = tuple(r1)

print(r1)
print(r2)