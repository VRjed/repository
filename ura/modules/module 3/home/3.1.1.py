text = input()
if text[0] and text[-1] == '"':
    print(text)
else:
    print('"' + text + '"')
