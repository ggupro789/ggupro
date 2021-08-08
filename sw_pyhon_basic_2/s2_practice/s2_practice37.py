# 다음의 결과와 같이 회문(앞뒤 어느 쪽에서도 같은 단어, 말) 여부를 판단하는 코드를 작성하십시오.

alpha = input()
result = ''.join(reversed(alpha))

if(alpha == result):
    print(result)
    print("입력하신 단어는 회문(Palindrome)입니다.")