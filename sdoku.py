import sys
import time

sudoku=[]
cnt=0
n=9
ans=[]
loop=0

def solve_sudoku(y,x): #재귀함수
    global loop
    global cnt
    global sudoku
    global n

    row=list(range(1,10))
    column=list(range(1,10))
    box=list(range(1,10))
    for i in sudoku[y]:
        if i==0:
            pass
        else:
            row.remove(i) #행에서 남은 수 구하기
    for i in range(n):
        if sudoku[i][x]==0:
            pass
        else:
            column.remove(sudoku[i][x]) #열에서 남은 수 구하기

    by=int(y/3)*3
    bx=int(x/3)*3 #속한 박스의 좌표를 구함
    for i in range(3):
        for j in range(3): 
            if sudoku[by+i][bx+j] ==0:
                pass
            else:
                box.remove(sudoku[by+i][bx+j]) #박스에서 남는 수 구하기 

    candidate= list((set(row) & set(column)) &set(box)) #칸에 들어갈 후보 구하기

    if not len(candidate): # 칸에 들어갈 후보가 없다면 돌아가기
        return

    sudoku[y][x]=candidate[0] #임시로 1번째 후보 채우기

    empty=[]

    for ey in range(n):
        for ex in range(n):
            if sudoku[ey][ex]==0:
                if (ey==y and ex>x) or ey>y:
                    empty.append([ey,ex]) #비어있는 블록 구하기

    for i in candidate:
        sudoku[y][x]=i

        if len(empty) ==0 : #다 채워졌다면 출력후 빠져나가기
            cnt+=1
            ans.append(sudoku)
            print(cnt)
            for i in sudoku:
                print(i)
            sudoku[y][x]=0
            
            # sys.exit()
        # for j in empty:
            # if (j[0]==y and j[1]>=x) or j[0]>y:
                # solve_sudoku(j[0],j[1]) #재귀
        else:
            solve_sudoku(empty[0][0],empty[0][1])
    
    sudoku[y][x]=0 #다시 칸 비우기
    return


f=open("s1.txt",'r')
str=f.readlines()
for line in str:
    sudoku.append(list(map(int,line.split(" "))))
i=0
ey,ex=0,0
empty=[]
for ey in range(n):
        for ex in range(n):
            if sudoku[ey][ex]==0:
                empty.append([ey,ex])
print("문제")
for i in sudoku:
    print(i)


solve_sudoku(empty[0][0],empty[0][1])

print("finish")