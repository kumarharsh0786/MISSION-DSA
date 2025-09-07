def count_jokes(dates):
    def base_to_decimal(num_str, base):
        if base <= 1:
            return -1
        decimal_value = 0
        for ch in num_str:
            digit = ord(ch) - ord('0')
            if digit < 0 or digit >= base:
                return -1
            decimal_value = decimal_value * base + digit
        return decimal_value

    count = 0
    n = len(dates)

    for i in range(n):
        M1, D1 = dates[i]
        for j in range(i + 1, n):
            M2, D2 = dates[j]

            val_D2_in_M1 = base_to_decimal(D2, M1)
            val_D1_in_M2 = base_to_decimal(D1, M2)

            if val_D2_in_M1 != -1 and val_D1_in_M2 != -1:
                if val_D2_in_M1 == int(D1) and val_D1_in_M2 == int(D2):
                    count += 1

    return count
