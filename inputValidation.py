import pyinputplus as pyip
# Different ways to use PyInputPlus for input validation

"""
# Can use arguments min, max, greaterThan, lessThan
response = pyip.inputNum("Enter a num: ", min=4)

# Blank not allowed by default, can use blank argument to allow.
response2 = pyip.inputNum("Test 2: ", blank=True)

# Can use limit and timeout arguments to limit attempts or timeout
# after a certain amount of seconds.
response3 = pyip.inputNum("Test 3: ", limit=3, timeout=60)

# Can use default argument to display error message rather than crashing.
response4 = pyip.inputNum("Test 4: ", limit=2, default='N/A')
print(response4)

# Can allow regular expressions or block them.
response5 = pyip.inputNum("Test 5: ", allowRegexes=[r'(I|V|X|L)+',r'zero'])
print(response5)

response6 = pyip.inputNum("Test 6: ", blockRegexes=[r'[02468]$'])
print(response6)
"""

# Custom function passed to inputCustom() for custom validation
"""
def addsUpToTen(numbers):
    numbersList = list(numbers)
    for i, digit in enumerate(numbersList):
        numbersList[i] = int(digit)
    if sum(numbersList) != 10:
        raise Exception('The digits must add up to 10, not %s.'%(sum(numbersList)))
    return int(numbers)

response7 = pyip.inputCustom(addsUpToTen)
"""

# Simple games with pyinputplus

"""
while True:
    prompt = 'Want to know how to keep an idiot busy for hours?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'no':
        break
print("Thank you. Have a nice day.")
"""







