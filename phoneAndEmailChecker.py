# Phone and Email lookup program
# Anthony Quinn
# 14/02/2021

import pyperclip, re

# Phone number regex
phoneRegex = re.compile(r'''(
(\d{3}|\(\d{3}\))?                # Area Code
(\s|-|\.)?                      # Seperator
(\d{3})                         # first 3 digits
(\s|-|\.)                       # Seperator
(\d{4})                         # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''', re.VERBOSE)

# Email regex
emailRegex = re.compile(r'''(
[a-zA-Z0-9._%+-]+   # Username
@                   # @ Symbol
[a-zA-Z0-9.-]+      # Domain name
(\.[a-zA-Z]{2,4})   # Dot
)''', re.VERBOSE)

# Find matches in clipboard.
text = str(pyperclip.paste())

matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No numbers or email addresses found.')

