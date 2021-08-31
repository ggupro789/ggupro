

def left(row,col,y):
    global sand

    r1,c1 = row-1,col
    r1_2,c1_2 = row+1,col

    r2,c2 = row-2,col-1
    r2_2,c2_2 = row+2,col-1

    r5,c5 = row,col-3
    
    r7,c7 = row-1,col-1
    r7_2,c7_2 = row+1,col-1
    
    r10,c10 = row-1,col-2
    r10_2,c10_2 = row+1,col-2
    
    ralpha,calpha = row,col-2

    alpha = 0
    alpha += persent1(r1,c1,y)
    alpha += persent1(r1_2,c1_2,y)
    alpha += persent2(r2,c2,y)
    alpha += persent2(r2_2,c2_2,y)
    alpha += persent5(r5,c5,y)
    alpha += persent7(r7,c7,y)
    alpha += persent7(r7_2,c7_2,y)
    alpha += persent10(r10,c10,y)
    alpha += persent10(r10_2,c10_2,y)

    if 0 <= ralpha < N and 0<= calpha < N:
        map_list[ralpha][calpha] += (y-alpha)
    else:
        sand += (y-alpha)
    
    map_list[row][col-1] = 0


    return row,col-1
        
def right(row,col,y):
    global sand

    r1,c1 = row-1,col
    r1_2,c1_2 = row+1,col

    r2,c2 = row-2,col+1
    r2_2,c2_2 = row+2,col+1

    r5,c5 = row,col+3
    
    r7,c7 = row-1,col+1
    r7_2,c7_2 = row+1,col+1
    
    r10,c10 = row-1,col+2
    r10_2,c10_2 = row+1,col+2
    
    ralpha,calpha = row,col+2

    alpha = 0
    alpha += persent1(r1,c1,y)
    alpha += persent1(r1_2,c1_2,y)
    alpha += persent2(r2,c2,y)
    alpha += persent2(r2_2,c2_2,y)
    alpha += persent5(r5,c5,y)
    alpha += persent7(r7,c7,y)
    alpha += persent7(r7_2,c7_2,y)
    alpha += persent10(r10,c10,y)
    alpha += persent10(r10_2,c10_2,y)

    if 0 <= ralpha < N and 0<= calpha < N:
        map_list[ralpha][calpha] += (y-alpha)
    else:
        sand += (y-alpha)
    
    map_list[row][col+1] = 0

    return row,col+1

def up(row,col,y):
    global sand

    r1,c1 = row,col-1
    r1_2,c1_2 = row,col+1

    r2,c2 = row-1,col-2
    r2_2,c2_2 = row-1,col+2

    r5,c5 = row-3,col
    
    r7,c7 = row-1,col-1
    r7_2,c7_2 = row-1,col+1
    
    r10,c10 = row-2,col-1
    r10_2,c10_2 = row-2,col+1
    
    ralpha,calpha = row-2,col
    alpha = 0
    alpha += persent1(r1,c1,y)
    alpha += persent1(r1_2,c1_2,y)
    alpha += persent2(r2,c2,y)
    alpha += persent2(r2_2,c2_2,y)
    alpha += persent5(r5,c5,y)
    alpha += persent7(r7,c7,y)
    alpha += persent7(r7_2,c7_2,y)
    alpha += persent10(r10,c10,y)
    alpha += persent10(r10_2,c10_2,y)

    if 0 <= ralpha < N and 0<= calpha < N:
        map_list[ralpha][calpha] += (y-alpha)
    else:
        sand += (y-alpha)

    map_list[row-1][col] = 0

    return row-1,col

def down(row,col,y):
    global sand
    r1,c1 = row,col-1
    r1_2,c1_2 = row,col+1

    r2,c2 = row+1,col-2
    r2_2,c2_2 = row+1,col+2

    r5,c5 = row+3,col
    
    r7,c7 = row+1,col-1
    r7_2,c7_2 = row+1,col+1
    
    r10,c10 = row+2,col-1
    r10_2,c10_2 = row+2,col+1
    
    ralpha,calpha = row+2,col
    alpha = 0
    alpha += persent1(r1,c1,y)
    alpha += persent1(r1_2,c1_2,y)
    alpha += persent2(r2,c2,y)
    alpha += persent2(r2_2,c2_2,y)
    alpha += persent5(r5,c5,y)
    alpha += persent7(r7,c7,y)
    alpha += persent7(r7_2,c7_2,y)
    alpha += persent10(r10,c10,y)
    alpha += persent10(r10_2,c10_2,y)

    if 0 <= ralpha < N and 0<= calpha < N:
        map_list[ralpha][calpha] += (y-alpha)
    else:
        sand += (y-alpha)

    map_list[row+1][col] = 0

    return row+1,col
#-------------------------------------------------  퍼센트 더하는 거
def persent1(row,col,y):
    global sand
    if 0 <= row < N and 0 <= col < N: 
        map_list[row][col] += int(y*0.01)
    else:
        sand += int(y*0.01)

    return int(y*0.01)

def persent2(row,col,y):
    global sand
    if 0 <= row < N and 0 <= col < N: 
        map_list[row][col] += int(y*0.02)
    else:
        sand += int(y*0.02)

    return int(y*0.02)

def persent5(row,col,y):
    global sand
    if 0 <= row < N and 0 <= col < N: 
        map_list[row][col] += int(y*0.05)
    else:
        sand += int(y*0.05) 

    return int(y*0.05)

def persent7(row,col,y):
    global sand
    if 0 <= row < N and 0 <= col < N: 
        map_list[row][col] += int(y*0.07)
    else:
        sand += int(y*0.07)

    return int(y*0.07)

def persent10(row,col,y):
    global sand 
    if 0 <= row < N and 0 <= col < N: 
        map_list[row][col] += int(y*0.1)
    else:
        sand += int(y*0.1)
    
    return int(y*0.1)
# -----------------------------------------------------------------------
N = int(input())
map_list = [list(map(int,input().split())) for _ in range(N)]
sand = 0

getleft = 1
getdown = 1
getright = 2
getup = 2

row,col = int(N-(N/2)),int(N-(N/2))

while True:
    rl,cl = 0,0
    rr,cr = 0,0
    ru,cu = 0,0
    rd,cd = 0,0

    for i in range(getleft):
        rl,cl = left(row,col,map_list[row][col-1])
        row,col = rl,cl
        if row == 0 and col == 0:
            break

    if row == 0 and col ==0:
        break


    for i in range(getdown):
        rd,cd = down(row,col,map_list[row+1][col])
        row,col = rd,cd

    for i in range(getright):
        rr,cr = right(row,col,map_list[row][col+1])
        row,col = rr,cr


    for i in range(getup):
        ru,cu = up(row,col,map_list[row-1][col])
        row,col = ru,cu

    getleft += 2
    getright += 2
    getdown += 2
    getup += 2

print(sand)