def nonDivisibleSubset(k, s):
    freq = [0] * k
    
    for num in s:
        freq[num % k] += 1
    result = 0
    if freq[0] > 0:
        result += 1
    for i in range(1, (k // 2) + 1):
        if i == k - i:  
            if freq[i] > 0:
                result += 1
        else:
            result += max(freq[i], freq[k - i])
    
    return result
