s = "a"

results = 1001
for char_length in range(1, len(s)//2+1):
    result = ""
    now = 0
    while now < len(s):
        now_char = s[now:now+char_length]
        count = 0
        if len(now_char) < char_length:
            result += now_char
            break
        while s[now+char_length:now+2*char_length] == now_char:
            now += char_length
            count += 1
            if now + char_length >= len(s):
                break
        if count:
            result += str(count+1)
        now += char_length
        result += now_char
    if results > len(result):
        results = len(result)

if results == 1001:
    print(1)
else:
    print(results)