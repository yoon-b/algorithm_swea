"""
중위 순회 -> 1부터 값을 1씩 증가시키며 저장

# 중위 순회의 기본 형태 (linked list를 활용한 트리 구현에서)
def inorderTraversal(self):
    if self.left:
        self.left.inorderTraversal()
    print(self.value)
    if self.right:
        self.right.inorderTraversal()

- left, right를 pointer가 아니라 인덱스로 접근하여 순회
- 해당 인덱스에서 값 입력
"""


def binarySearchTree(tree: list, i: int):
    global insrt
    if i <= N:
        binarySearchTree(tree, i*2)
        tree[i] = insrt
        insrt += 1
        binarySearchTree(tree, i*2+1)
    return tree


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    bTree = [0] * (N+1)
    insrt = 1  # insert 할 값
    binarySearchTree(bTree, 1)  # 1번 인덱스부터 시작
    root = bTree[1]
    nodeHalfN = bTree[N//2]

    print(f'#{tc}', root, nodeHalfN)
