
class SortedRoster:
    def __init__(self):
        self.roster = []
        
    def add_player(self, student_id):
        index = self._find_insert_position(student_id)
        self.roster.insert(index, student_id)
        
    def find_player(self, student_id):
        left, right = 0, len(self.roster) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.roster[mid] == student_id:
                return True
            elif self.roster[mid] < student_id:
                left = mid + 1
            else:
                right 
