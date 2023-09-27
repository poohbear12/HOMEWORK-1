import copy
import numpy as np
import Utils as ul

def get_result(row,col,board,dir_arr):
    global result_arr
    for i in range(row,len(board[0])):
        for j in range(col,len(board[0])):
            if board[i][j] != 0:
                if i==8 and j==8:
                    result_arr[dir_arr].append(copy.deepcopy(board))
                    return False
                elif j==8:
                    col=0
                    break
                continue
            for k in ul.optional_array(i,j,board):
                    board[i][j] = k
                    if get_result(i,j,board,dir_arr) == False:
                        board[i][j] = 0
            return False
def last_result(row,col,board,a,b,c,d):
    global kk
    global instr
    for i in range(row,len(board[0])):
        for j in range(col,len(board[0])):
            if board[i][j]!=0:
                if i==8&j==8:
                    kk = kk +1
                    temp = copy.deepcopy(ls)
                    ul.add_arr(temp,a,b,c,d,board,result_arr)
                    ul.writeExcel("data/这是："+ str(instr)[5:11] +"的第" + str(kk) + "次结果"+".xlsx", temp)
                    print("这是第："+str(kk)+"种解法")
                    return False
                elif j==8:
                    col=0
                    break
                continue
            for k in ul.optional_array(i,j,board):
                    board[i][j] = k
                    if last_result(i,j,board,a,b,c,d) == False:
                        board[i][j] = 0
            return False
def combination_block(ls):

    # 右上
    get_result(0,0,ul.deconstruction_arr(ls,'q'),0)

    # 左上
    get_result(0,0,ul.deconstruction_arr(ls,'w'),1)

    # 右下
    get_result(0,0,ul.deconstruction_arr(ls,'e'),2)

    # 左下
    get_result(0,0,ul.deconstruction_arr(ls,'r'),3)
def reduce_repeat(result,block):
    # 左上
    for i in range(len(result[0])):
        block[0].append(copy.deepcopy(ul.de_part(result[0][i],'r')))
    block[0] = np.array(block[0])
    block[0] = np.unique(block[0],axis=0)

    #右上
    for i in range(len(result[1])):
        block[1].append(copy.deepcopy(ul.de_part(result[1][i],'e')))
    block[1] = np.array(block[1])
    block[1] = np.unique(block[1],axis=0)

    for i in range(len(result[2])):
        block[2].append(copy.deepcopy(ul.de_part(result[2][i],'w')))
    block[2] = np.array(block[2])
    block[2] = np.unique(block[2],axis=0)

    for i in range(len(result[3])):
        block[3].append(copy.deepcopy(ul.de_part(result[3][i],'q')))
    block[3] = np.array(block[3])
    block[3] = np.unique(block[3],axis=0)
def last_mid():
    mid_arr = []
    for i in range(6, 6 + 9):
        mid_arr.append(ls[i][6:6 + 9])
    for i in range(len(part_arr[0])):
        for j in range(len(part_arr[1])):
            fl = False
            for k in range(len(part_arr[2])):
                if fl:
                    break
                for z in range(len(part_arr[3])):
                    temp_arr = copy.deepcopy(mid_arr)
                    temp_arr = ul.compat(part_arr[0][i], part_arr[1][j], part_arr[2][k], part_arr[3][z], temp_arr)
                    if temp_arr == None:
                        continue
                    b = ul.judge_is_legal(temp_arr)
                    if b==-1:
                        last_result(0,0,temp_arr,i,j,k,z)
                    elif b>-1 and b<3:
                        fl = True
                        break
                    elif b>8 and b<12:
                        break

if __name__ == '__main__':
    instr = "data/input1.xlsx"
    ls = ul. readExcel(instr, 0, 0)
    result_arr = [list(),list(),list(),list()]
    part_arr = [list(),list(),list(),list()]
    kk = 0
    combination_block(ls)
    reduce_repeat(result_arr,part_arr)
    last_mid()

