s = "azcbobobegghakl"

longest = ""

current = s[0]

for i in range(1, len(s)):
    if s[i] >= s[i - 1]:
        current += s[i]
    else:
        if len(current) > len(longest):
            longest = current
        current = s[i]


if len(current) > len(longest):
    longest = current

print(longest)