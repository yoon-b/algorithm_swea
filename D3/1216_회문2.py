def palindrome(word):
    rev = word[::-1]
    if word == rev:
        return 1
    else:
        return 0
 
for _ in range(10):
    tc = int(input())
    arr = [input() for _ in range(100)]
    arr_t = list((zip(*arr)))  # transpose
    arrT = [[0] for _ in range(100)]
 
    for i in range(100):
        arrT[i] = ''.join(arr_t[i])
 
    maxP = 0
 
    for row in arr:  # 각 행에 대해
        found = 0
        for i in range(100, 0, -1):  # 길이 긴 순서부터 확인
            for j in range(100 - i + 1):  # 시작 인덱스의 범위
                if palindrome(row[j:j+i]):  # 회문인 경우
                    found = 1
                    if maxP < i: #회문의 길이
                        maxP = i  # 최댓값 갱신
                    break  # 더 짧은 길이 확인할 필요 없음
            if found:  # 찾았으면 다음 행 검사
                break
 
    for row in arrT:  # 전치 행렬의 행 = 원본의 열
        found = 0
        for i in range(100, 0, -1):
            for j in range(100 - i + 1):
                if palindrome(row[j:j + i]):
                    found = 1
                    if maxP < i:
                        maxP = i
                    break
            if found:
                break
 
    print(f'#{tc} {maxP}')