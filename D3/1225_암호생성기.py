class ListNode:
    def __init__(self, val, nxt, prev):
        self.val, self.nxt, self.prev = val, nxt, prev


class CircularQ:
    def __init__(self):
        self.left = ListNode(-1, None, None)
        self.right = ListNode(-1, None, self.left)

    def enQueue(self, value: int):
        cur = ListNode(value, self.right, self.right.prev)
        self.right.prev.nxt = cur
        self.right.prev = cur
        return True

    def deQueue(self):
        self.left.nxt = self.left.nxt.nxt
        self.left.prev = self.left 


for _ in range(10):
    tc = int(input())
    nums = list(map(int, input().split()))
    cq = CircularQ()
    for n in nums:
        cq.enQueue(n)
    cntZero = 0

    while cntZero == 0:
        for i in range(1, 6):
            pw = cq.left.nxt.val - i
            cq.deQueue()
            if pw <= 0:
                cq.enQueue(0)
                cntZero += 1
                break
            cq.enQueue(pw)

    password = []
    elem = cq.left.nxt
    for _ in range(8):
        password.append(elem.val)
        elem = elem.nxt

    print(f'#{tc}', *password)