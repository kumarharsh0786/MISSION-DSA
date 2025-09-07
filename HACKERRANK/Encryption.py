def encryption(s):
    s = s.replace(" ", "")
    length = len(s) 
    rows = math.floor(math.sqrt(length))
    cols = math.ceil(math.sqrt(length))
    if rows * cols < length:
        rows += 1
    grid = []
    for i in range(0, length, cols):
        grid.append(s[i:i+cols])
    encrypted_words = []
    for col in range(cols):
        word = []
        for row in range(rows):
            if col < len(grid[row]):
                word.append(grid[row][col])
        encrypted_words.append(''.join(word))
    
    return ' '.join(encrypted_words)
