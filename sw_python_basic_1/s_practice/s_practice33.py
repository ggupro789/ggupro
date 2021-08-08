word = str(input())

def reverse(x):
    result = "".join(reversed(word))
    print("{0}".format(result))
    if(word == result):
        print("입력하신 단어는 회문(Palindrome)입니다.")
    else:
        print("입력하신 단어는 회문(Palindrome)이 아닙니다.")

reverse(word)