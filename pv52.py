class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None

    # Tạo một bộ để lưu trữ các tham chiếu của các nút từ danh sách liên kết A
    nodes_set = set()

    # Lưu trữ tham chiếu của các nút từ danh sách liên kết A vào bộ
    current = headA
    while current:
        nodes_set.add(current)
        current = current.next

    # Kiểm tra từng nút từ danh sách liên kết B
    current = headB
    while current:
        # Nếu nút hiện tại đã xuất hiện trong bộ, chúng giao nhau
        if current in nodes_set:
            return current
        current = current.next

    # Nếu không có nút giao nhau
    return None

# Example usage:
# Tạo danh sách liên kết A
headA = ListNode(4)
nodeA1 = ListNode(1)
nodeA2 = ListNode(8)
nodeA3 = ListNode(4)
nodeA4 = ListNode(5)
headA.next = nodeA1
nodeA1.next = nodeA2
nodeA2.next = nodeA3
nodeA3.next = nodeA4

# Tạo danh sách liên kết B
headB = ListNode(5)
nodeB1 = ListNode(0)
nodeB2 = ListNode(1)
headB.next = nodeB1
nodeB1.next = nodeB2
# Gán nút cuối của danh sách B với nút kế cuối của danh sách A
nodeB2.next = nodeA2

# Kiểm tra nút giao nhau
intersection_node = getIntersectionNode(headA, headB)
if intersection_node:
    print("Có nút giao nhau. Giá trị của nút giao nhau là:", intersection_node.value)
else:
    print("Không có nút giao nhau.")
