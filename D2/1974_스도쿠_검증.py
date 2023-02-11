T = int(input())
 
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
 
    for i in range(9):
        checkH = [0] * 9  # 행
        checkV = [0] * 9  # 열
        for j in range(9):
            checkH[j] = sudoku[i][j]
            checkV[j] = sudoku[j][i]
        if len(set(checkH)) != 9:  # 행에 중복값
            result = 0
            break
        elif len(set(checkV)) != 9:  # 열에 중복값
            result = 0
            break
        else:
            result = 1
 
    if result:  # 행, 열에 문제 없으면
        for i in range(0, 9, 3):  # 3x3 배열 확인
            for j in range(0, 9, 3):
                check = []
                for x in range(3):
                    for y in range(3):
                        check.append(sudoku[i + x][j + y])
                if len(set(check)) != 9:
                    result = 0
                    break
                else:
                    result = 1
            if not result:
                break
    print(f'#{tc} {result}')