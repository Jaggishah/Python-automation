import pyperclip
# from pyperclip import paste
# pyperclip.copy('The text to be copied to the clipboard.')
text = pyperclip.paste()
# print(text)
lines = text.split('\n')

for i in range(len(lines)):
    lines[i] = '*' + lines[i]

final = '\n'.join(lines)
pyperclip.copy(final)

