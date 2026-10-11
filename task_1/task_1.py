import re

s = input("Введите строку: ")
text = s[1:- 1]

words = re.findall(r'\S+', text)

words_reversed = ""
for i in range(len(words) - 1, -1, -1):
    words_reversed += words[i] + " "

string_reversed = ""
for i in range(len(text) - 1, -1, -1):
    string_reversed += text[i]

print(s, "-", "«" + words_reversed[:-1] + "»")
print(s, "-", "«" + string_reversed + "»")