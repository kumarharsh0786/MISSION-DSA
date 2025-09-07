def toys(w):
    w.sort()
    containers = 0
    i = 0
    n = len(w)
    while i < n:
        containers += 1
        limit = w[i] + 4  
        i += 1
        while i < n and w[i] <= limit:
            i += 1
    
    return containers
