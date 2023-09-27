import xlrd
import xlsxwriter
import copy
'''
   读取excel文件并转为list返回
   :param filename: 文件名
   :param row:
   :param col:
   :return 21x21 array:
'''
def readExcel(filename, row, col):
    workbook = xlrd.open_workbook(filename)
    sheetdata = workbook.sheet_by_name('Sheet1')
    # print(sheetData)
    ls = []
    for i in range(row, row + 21):
        lt = []
        for j in range(col, col + 21):
            if sheetdata.cell(i, j).value == 0.0:
                lt.append(0)
            elif sheetdata.cell(i, j).value == '':
                lt.append('*')
            else:
                lt.append(int(sheetdata.cell(i, j).value))
        ls.append(lt)
    return ls

"""
        读取excel文件并转为list返回
        :param ls:
        :param filename: 文件名
        :return:
"""
def writeExcel(filename, ls):
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet("Sheet1")
    worksheet.activate()  # 激活工作表
    i = 1
    while i <= len(ls):
        row = 'A' + str(i)
        lt = ls[i - 1]
        for j in range(len(lt)):
            if lt[j] == "*":
                lt[j] = ''
        worksheet.write_row(row, lt)
        i += 1
    workbook.close()

def optional_array(row,col,board):
    base_arr = list(range(1,10))
    exist_arr = []
    for i in range(len(board[row])):
        exist_arr.append(board[i][col])
        exist_arr.append(board[row][i])
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            exist_arr.append(board[i][j])
    return set(base_arr).difference(exist_arr)

def deconstruction_arr(ls,dire):
    board = []
    if dire == 'q':
        for i in range(0, 9):
            board.append(ls[i][0:9])
    elif dire == 'w':
        for i in range(0, 9):
            board.append(ls[i][12:21])
    elif dire =='e':
        for i in range(0, 9):
            board.append(ls[i+12][0:9])
    elif dire =='r':
        for i in range(0, 9):
            board.append(ls[i+12][12:21])
    return board

def de_part(arr,dire):
    if dire=='q':
        temp = list()
        for i in range(3):
            temp.append(arr[i][0:3])
        return temp
    elif dire=='w':
        temp = list()
        for i in range(3):
            temp.append(arr[i][6:9])
        return temp
    elif dire=='e':
        temp = list()
        for i in range(3):
            temp.append(arr[6+i][0:3])
        return temp
    elif dire=='r':
        temp = list()
        for i in range(3):
            temp.append(arr[6+i][6:9])
        return temp
def compat(arr1,arr2,arr3,arr4,let):
    let1 = copy.deepcopy(let)
    for i in range(3):
        for j in range(3):
            if let1[i][j] != 0:
                if let1[i][j] != arr1[i][j]:
                    return None
            let1[i][j] = arr1[i][j]
    for i in range(3):
        for j in range(3):
            if let1[i][j+6] != 0:
                if let1[i][j+6] != arr2[i][j]:
                    return None
            let1[i][j+6] = arr2[i][j]
    for i in range(3):
        for j in range(3):
            if  let1[i+6][j] != 0:
                if let1[i+6][j] != arr3[i][j]:
                    return None
            let1[i+6][j] = arr3[i][j]
    for i in range(3):
        for j in range(3):
            if let1[6 + i][6+j] != 0:
                if let1[6 + i][6+j] != arr4[i][j]:
                    return None
            let1[6 + i][6+j] = arr4[i][j]
    return let1

def judge_is_legal(board):
    length = len(board[0])
    for i in range(length):
        arr = []
        arr = board[i]
        arr = [i for i in arr if i != 0]
        if len(arr)!= len(set(arr)):
            return i
    for i in range(length):
        arr = []
        for j in range(length):
            arr.append(board[j][i])
        arr = [i for i in arr if i!=0]
        if len(arr) != len(set(arr)):
            return i+9
    # for i in [0,3,6]:
    #     for j in [0,3,6]:
    #         start_row = (i // 3) * 3
    #         start_col = (j // 3) * 3
    #         arr = []
    #         for i in range(start_row, start_row + 3):
    #             for j in range(start_col, start_col + 3):
    #                 arr.append(board[i][j])
    #         arr = [i for i in arr if i!=0]
    #         if len(arr)!=len(set(arr)):
    #             return False

    return -1

def add_arr(ls,a,b,c,d,board,result_arr):
    for i in range(9):
        for j in range(9):
            ls[i][j] = result_arr[0][a][i][j]
    for i in range(9):
        for j in range(9):
            ls[i][j+12] = result_arr[1][b][i][j]
    for i in range(9):
        for j in range(9):
            ls[i+12][j] = result_arr[2][c][i][j]
    for i in range(9):
        for j in range(9):
            ls[i+12][j+12] = result_arr[3][d][i][j]
    for i in range(9):
        for j in range(9):
            ls[i+6][j+6] = board[i][j]


if __name__ == '__main__':
    ls = readExcel("data/input3.xlsx", 0, 0)
    deconstruction_arr(ls,'q')
    deconstruction_arr(ls,'w')
    deconstruction_arr(ls,'e')
    deconstruction_arr(ls,'r')
