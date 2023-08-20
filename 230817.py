# 백준 28706번 : 럭키 세븐
import sys
input = sys.stdin.readline

# t : 테스트 케이스 수
t = int(input())

testCase = []
for i in range(t):
    # n : 각 케이스의 턴 수
    n = int(input())
    
    dpSet = set([1])

    for j in range(n):
        op1, v1, op2, v2 = map(str, input().split())
        temp = set()
        for k in dpSet:
            if op1 == "*":
                temp.add((k * int(v1)) % 7)
            elif op1 == "+":
                temp.add((k + int(v1)) % 7)
            if op2 == "*":
                temp.add((k * int(v2)) % 7)
            elif op2 == "+":
                temp.add((k + int(v2)) % 7)
        dpSet = temp
    if 0 in dpSet:
        print("LUCKY")
    else:
        print("UNLUCKY")