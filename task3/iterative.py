def find_maximum_iterative(node):
    if node is None:
        return float('-inf')
        
    current_max = node.price
    current = node.next
    
    while current is not None:
        if current.price > current_max:
            current_max = current.price
        current = current.next
        
    return current_max
