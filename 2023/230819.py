# 백준 10026번 : 적록 색약
import sys
input = sys.stdin.readline

# n : 그리드의 크기
n = int(input())

# pic : 그림
pic = []
colorLessPic = []
for i in range(n):
    input_pic = list(input().strip())
    pic.append(input_pic)
    less_pic = []
    for j in input_pic:
        if j == "G" or j == "R":
            less_pic.append("G")
        else:
            less_pic.append("B")
    colorLessPic.append(less_pic)

colorVisited = [[False for j in range(n)] for i in range(n)]
colorLessVisted = [[False for j in range(n)] for i in range(n)]
colorCnt = 0
colorLessCnt = 0

def colorCheck(cnt, pic, visited, i, j, n):
    visited[i][j] = True
    partColor = pic[i][j]
    isFirst = True
    if i == 0 and j == 3:
        print("i, j :", i, j)
    if i - 1 >= 0 and pic[i - 1][j] == partColor:
        if not visited[i - 1][j]:
            colorCheck(cnt, pic, visited, i - 1, j, n)
        else:
            if i == 0 and j == 3:
                print("i - 1 here")
            isFirst = False
    if j + 1 < n and pic[i][j + 1] == partColor:
        if not visited[i][j + 1]:
            colorCheck(cnt, pic, visited, i, j + 1, n)
        else:
            if i == 0 and j == 3:
                print("j + 1 here")
            isFirst = False
    if i + 1 < n and pic[i + 1][j] == partColor:
        if not visited[i + 1][j]:
            colorCheck(cnt, pic, visited, i + 1, j, n)
        else:
            if i == 0 and j == 3:
                print("i + 1 here")
            isFirst = False
    if j - 1 >= 0 and pic[i][j - 1] == partColor:
        if not visited[i][j - 1]:
            colorCheck(cnt, pic, visited, i, j - 1, n)
        else:
            if i == 0 and j == 3:
                print("j - 1 here")
            isFirst = False
    if i == 0 and j == 3:
        print("isFirst :", isFirst)
    if isFirst:
        cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        print("i :", i, "j :", j)
        if not colorVisited[i][j]:
            colorCnt = colorCheck(colorCnt, pic, colorVisited, i, j, n)
        elif not colorLessVisted[i][j]:
            colorLessCnt = colorCheck(colorLessCnt, colorLessPic, colorLessVisted, i, j, n)
        
        print("colorCnt :", colorCnt)
        print("colorVisited")
        print(colorVisited)
        print("colorLessCnt :", colorLessCnt)
        print("colorLessVisted")
        print(colorLessVisted)
        print()

print(colorCnt, colorLessCnt)
