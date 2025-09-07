def sherlockAndAnagrams(s):
    from collections import defaultdict
    
    substr_freq = defaultdict(int)
    n = len(s)
     
    for length in range(1, n):
        for start in range(n - length + 1):
            substring = s[start:start+length]
            sorted_sub = ''.join(sorted(substring))
            substr_freq[sorted_sub] += 1
    count = 0
    for freq in substr_freq.values():
        if freq > 1:
            count += (freq * (freq - 1)) // 2
    return count
