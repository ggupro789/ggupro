# ABBA처럼 어느 방향에서 읽어도 같은 문자열을 회문이라 한다. NxN 크기의 글자판에서 길이가 M인 회문을 찾아 출력하는 프로그램을 만드시오.
# 회문은 1개가 존재하는데, 가로 뿐만 아니라 세로로 찾아질 수도 있다.


import collections
from typing import Collection, Deque


test_case= int(input())

def palindrome(s:str):
    strs:Deque = collections.deque()
    for char in s:
        strs.append(char)

    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False
    
    return True

for i in range(test_case):
    NM = list(map(int,input().split()))
    str = [] #가로
    str2 = [] # 세로

    for j in range(NM[0]):
        str.append(input())

    for k in range(len(str)):
        temp = ''
        for l in range(len(str)):
            temp += str[l][k]

        str2.append(temp)
    
    
    
    