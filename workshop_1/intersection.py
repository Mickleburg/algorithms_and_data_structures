class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = new_node

def intersection(headA: LList, headB: LList) -> Node | None :
    curA = headA.head
    curB = headB.head

    while curA.data != curB.data:

        if curA is None:
            curA = headB.head
        else:
            curA = curA.next
        
        if curB is None:
            curB = headA.head
        else:
            curB = curB.next
    
    return curA

listA = LList()
listB = LList()

listA.append(4)
listA.append(1)
listA.append(8)
listA.append(4)
listA.append(5)

listB.append(5)
listB.append(6)
listB.append(8)
listB.append(4)
listB.append(5)

rez = intersection(listA, listB)
assert rez.data == 8, "Ошибка"

print("OK")