str = "shankarsinghaswal"

unique_chars = ""
for char in str:
    if str.count(char) == 1:
        unique_chars += char
print("char is:", unique_chars )