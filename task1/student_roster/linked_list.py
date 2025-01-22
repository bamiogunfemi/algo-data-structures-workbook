class Node:
    def __init__(self, student_id):
        self.student_id = student_id
        self.next = None

class LinkedRoster:
    def __init__(self):
        self.head = None
        
    def add_player(self, student_id):
        new_node = Node(student_id)
        new_node.next = self.head
        self.head = new_node
