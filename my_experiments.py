def double_char(s):
    result = ''
    i = 0
    while i < len(s):
        result = result + s[i] * 2
        i += 1
    print(result)

double_char('World is empty!')