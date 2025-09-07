def highestValuePalindrome(s, n, k):
    s = list(s)
    changed = [False] * n
    left, right = 0, n - 1
    changes_used = 0
    while left < right:
        if s[left] != s[right]:
            higher = max(s[left], s[right])
            s[left] = s[right] = higher
            changed[left] = changed[right] = True
            changes_used += 1
        left += 1
        right -= 1

    if changes_used > k:
        return "-1"

    left, right = 0, n - 1
    spare_changes = k - changes_used
    while left <= right:
        if left == right:  
            if spare_changes > 0 and s[left] != '9':
                s[left] = '9'
                spare_changes -= 1
        else:
            if s[left] != '9':
                if changed[left] or changed[right]:
                    if spare_changes > 0:
                        s[left] = s[right] = '9'
                        spare_changes -= 1
  
                    if spare_changes > 1:
                        s[left] = s[right] = '9'
                        spare_changes -= 2
        left += 1
        right -= 1

    return "".join(s)
