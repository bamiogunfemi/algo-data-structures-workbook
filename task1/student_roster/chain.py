class ChainNode:
    def __init__(self, student_id):
        self.student_id = student_id
        self.next = None
        self.prev = None

class ChainRoster:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_player(self, student_id):
        new_node = ChainNode(student_id)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
