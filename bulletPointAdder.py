# Bullet Point Adding Program
# Adding wikipedia bullet points to the start
# of each line of text on the clipboard.
# Anthony Quinn - 13/02/2021

import pyperclip

text = pyperclip.paste()

# Separate lines and add stars.
lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)

pyperclip.copy(text)
