class HeapRoster:
    def __init__(self):
        self.heap = []
        
    def add_player(self, student_id):
        self.heap.append(student_id)
        self._sift_up(len(self.heap) - 1)
