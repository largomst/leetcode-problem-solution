
import tqdm
from random import choice, randint


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class List:
    def __init__(self) -> None:
        self.head = None

    def addHead(self, val):
        new = ListNode(val)
        new.next = self.head
        self.head = new

    def addTail(self, val):
        prev = None
        cur = self.head
        while cur:
            prev = cur
            cur = cur.next

        new = ListNode(val)
        if prev:
            prev.next = new
        else:
            self.head = new


def genRandomNodeList():
    l = List()
    size = randint(0, 100)
    cur = l.head
    i = 0
    while i < size:
        val = randint(0, 100)
        node = ListNode(val)
        if cur == None:
            cur = node
            l.head = cur
        else:
            cur.next = node
            cur = cur.next
        i += 1
    return l.head, False


def genRandomCyclicNodeList():
    l = List()
    size = randint(1, 100)
    cur = l.head
    created = {}
    i = 0
    while i < size:
        val = randint(0, 100)
        node = ListNode(val)
        created[node] = node
        if cur == None:
            cur = node
            l.head = cur
        else:
            cur.next = node
            cur = cur.next
        if i == size-1:  # 随机选择结点创建环
            cur.next = created.get(choice(list(created.keys())))
        i += 1
    return l.head, True


def genRandomNodeListWithIndex():
    l = List()
    size = randint(0, 100)
    cur = l.head
    i = 0
    while i < size:
        val = randint(0, 100)
        node = ListNode(val)
        if cur == None:
            cur = node
            l.head = cur
        else:
            cur.next = node
            cur = cur.next
        i += 1
    return l.head, None


def genRandomCyclicNodeListWithIndex():
    l = List()
    size = randint(1, 100)
    cur = l.head
    created = {}
    answer = None
    while i < size:
        val = randint(0, 100)
        node = ListNode(val)
        created[node] = node
        if cur == None:
            cur = node
            l.head = cur
        else:
            cur.next = node
            cur = cur.next
        if i == size-1:  # 随机选择结点创建环
            answer = choice(list(created.keys()))
            cur.next = created.get(answer)
    return l.head, answer


def hasCycleComparar(func, times=500_000):
    gen = choice([genRandomCyclicNodeList, genRandomNodeList])
    correct = 0

    for i in tqdm.tqdm(range(times)):
        l, r = gen()
        if func(l) == r:
            correct += 1
    print('Correct rate:', correct / times*100, '%')
