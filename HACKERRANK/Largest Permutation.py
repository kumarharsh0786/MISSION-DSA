def largestPermutation(k, arr):
    n = len(arr) 
    index_map = {val: idx for idx, val in enumerate(arr)}
    for i in range(n):
        if k <= 0:
            break
        desired_val = n - i  
        if arr[i] == desired_val:
            continue  
        desired_idx = index_map[desired_val]
        index_map[arr[i]] = desired_idx
        index_map[desired_val] = i
        arr[i], arr[desired_idx] = arr[desired_idx], arr[i]
        k -= 1
    return arr
