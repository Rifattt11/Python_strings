import re

text = ""
while '.' not in text:
    text += input() + " "

text = re.match(r'[^.]*\.', text).group()

words = re.findall(r'[A-Za-z]+', text)
k = 0
for word in words:
    if len(word) > k:
        k = len(word)

result = ""
for ch in text:
    if 'a' <= ch <= 'z':
        result += bytes([(ch.encode()[0] - 97 + k) % 26 + 97]).decode()
    elif 'A' <= ch <= 'Z':
        result += bytes([(ch.encode()[0] - 65 + k) % 26 + 65]).decode()
    else:
        result += ch

print(result)
print(k)