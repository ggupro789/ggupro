import collections
import re

def isPalindrome(words:str):
    deq = collections.deque()
    for chr in words:
        if chr.isalpha():
            deq.append(chr.lower())
    while len(deq) > 1:
        if deq.pop() != deq.popleft():
            return False
    
    return True
# -------------------------------------------------  deque 활용
def isPalindrome(words:str):
    words.lower()
    
    words = re.sub('[^a-z0-9]', '',words)
    return words == words[::-1]
# ------------------------------------------------- 문자열 슬라이싱 활용
word = list(input())
word_list = []
for i in range(len(word)):
    if word[i].isalpha() == True:
        word_list.append(word[i].lower())

if word_list == list(reversed(word_list)):
    print(True)
else:
    print(False)

# word = input()
# print(isPalindrome(word))