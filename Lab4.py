"""
Anthony Quinn
X00138635
Lab Exercises - Functions
"""
import csv
total = 0
counter = 0

with open('pima.csv', 'r', newline='') as file:
    bloodPressure = list(csv.reader(file))

print(bloodPressure)
for entry in bloodPressure:
    print(entry)
    for number in entry:
        if number != 0:
            total += float(number)
            counter += 1

average = total / counter
average = round(average, 2)
print(total)
print("Average blood pressure:", average)

file.close()

for entry in bloodPressure:
    if entry[2] == '0':
        entry[2] = average
print(bloodPressure)

with open('pimaNew.csv', 'w+') as new_file:
    write = csv.writer(new_file)

    write.writerows(bloodPressure)

"""
# Q2
import random

def number():
    print(random.randint(0, 100))

for i in range(10):
    number()

# Q3
limit = int(input("Limit: "))

def oddGenerator(number):
    for i in range(limit):
        odd = i % 2
        if odd != 0:
            print(i)

oddGenerator(limit)

# Q4
first = input('First word: ')
second = input('Second word: ')

def longerString(string1, string2):
    if string1 > string2:
        print("First word", string1, "is longer than", string2)
    else:
        print("Second word", string2, "is longer than", string1)

longerString(first, second)
"""
