# USA Phone Number Format Validation
# Anthony Quinn
# 13/02/2021

import re

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True


# Basic checking
print("Is 415-555-4242 a phone number?")
print(isPhoneNumber('415-555-4242')) # Will return true.
print(isPhoneNumber('Moshi')) # Will return false.

# Parsing through a user input sentence for number.
print("Enter a message with or without phone number format for checking:")
message = input()
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done.')


# Using regex (regular expressions to simplify the above)

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
regex_test = phoneNumRegex.search(message)
print('Phone number found [regex]: ' + regex_test.group())
areaCode, mainNumber = regex_test.groups()
print('Area Code: ' + areaCode)
print('Rest of number: ' + mainNumber)

# findall() method and regex

list = []
phoneNumRegexEdit = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
list = phoneNumRegexEdit.findall(message)
print(list)

