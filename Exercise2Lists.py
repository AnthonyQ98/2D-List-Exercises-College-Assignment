table = [[10.5, 12.0, 14.5, 16.75, 18.0],
         [20.5, 22.25, 24.0, 26.25, 28.0],
         [34.0, 36.5, 38.0, 40.35, 43.0],
         [50.0, 60.0, 70.0, 80.0, 99.99]]

print("\t\t\t\t\tPayscale Table")
print("\t\t Step 1\t Step 2\t Step 3\t Step 4\t Step 5")
print("_" * 50)
for i, row in enumerate(table):
    for index, object in enumerate(row):
        if index == 0:
            print("Grade :{0}{1:8}".format(i+1, object), end="")
        else:
            print("{:8}".format(object), end="")
    print()

# Q1
total = 0
for item in table[2]:
    total += item
average = total / len(table[2])
print(average)

# Q2
for i, item in enumerate(table):
    total = 0
    for number in item:
        total += number
    average_each_grade = total / len(item)
    print("Average for Grade {}: ".format(i+1), average_each_grade)
    print("Total for Grade {}: ".format(i+1), total)

# Q3
for i, item in enumerate(table):
    difference = max(item) - min(item)
    print("Difference between highest and lowest steps of Grade {} is: ".format(i+1), round(difference, 2))

# Q4 is at the top.

# Q5

print("\t\t\t\t\tPayscale Table")
print("\t\t Step 1\t Step 2\t Step 3\t Step 4\t Step 5")
print("_" * 50)
for i, row in enumerate(table):
    for index, object in enumerate(row):
        if index == 0:
            print("Grade :{0}{1:8}".format(i+1, object + 1.50), end="")
        else:
            print("{:8}".format(object + 1.50), end="")
    print()
