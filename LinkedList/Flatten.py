def flatten(root):
    if(root == None or root.next == None):
        return root
    root = merge(root, flatten(root.next))
    return root

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    
    result = None
    if (a.data < b.data):
        result = a
        result.bottom = merge(a.bottom, b)
    else:
        result = b
        result.bottom = merge(a, b.bottom)

    result.right = None
    return result

