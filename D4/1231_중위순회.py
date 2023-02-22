def inorderTraversal(idx):
    global ans
    if len(tree[idx]) >= 2:
        inorderTraversal(int(tree[idx][1]))
    ans += tree[idx][0]
    if len(tree[idx]) >= 3:
        inorderTraversal(int(tree[idx][2]))


for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N):
        idx, *node = input().split()
        tree[int(idx)].extend([*node])
    ans = ''
    inorderTraversal(1)

    print(f'#{tc}', ans)