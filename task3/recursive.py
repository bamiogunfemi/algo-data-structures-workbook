def find_maximum_recursive(node):
    if node is None:
        return float('-inf')
    
    max_remaining = find_maximum_recursive(node.next)
    return max(node.price, max_remaining)
