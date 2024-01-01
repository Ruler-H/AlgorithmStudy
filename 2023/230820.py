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
    iterList = []
    if i - 1 >= 0 and pic[i - 1][j] == partColor:
        if visited[i - 1][j]:
            isFirst = False
        else:
            iterList.append([i - 1, j])
    if j + 1 < n and pic[i][j + 1] == partColor:
        if visited[i][j + 1]:
            isFirst = False
        else:
            iterList.append([i, j + 1])
    if i + 1 < n and pic[i + 1][j] == partColor:
        if visited[i + 1][j]:
            isFirst = False
        else:
            iterList.append([i + 1, j])
    if j - 1 >= 0 and pic[i][j - 1] == partColor:
        if visited[i][j - 1]:
            isFirst = False
        else:
            iterList.append([i, j - 1])
    for it in iterList:
        colorCheck(cnt, pic, visited, it[0], it[1], n)
    if isFirst:
        cnt += 1

    return cnt


for i in range(n):
    for j in range(n):
        print("i :", i, "j :", j)
        if not colorVisited[i][j]:
            colorCnt = colorCheck(colorCnt, pic, colorVisited, i, j, n)
        if not colorLessVisted[i][j]:
            colorLessCnt = colorCheck(colorLessCnt, colorLessPic, colorLessVisted, i, j, n)
        
        print("colorCnt :", colorCnt)
        print("colorVisited")
        print(colorVisited)
        print("colorLessCnt :", colorLessCnt)
        print("colorLessVisted")
        print(colorLessVisted)
        print()

print(colorCnt, colorLessCnt)
