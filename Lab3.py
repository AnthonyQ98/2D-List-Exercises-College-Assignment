"""
Anthony Quinn
X00138635
Lab Exercises - Writing to files, reading from files
"""



count = 0

with open('names.txt', 'a+') as output_file:
    content_output = output_file.readlines()
    while count < 5:
        name = input("Name: ")
        while len(name) < 10:
            name = input("Name must be at least 10 characters, retry: ")
        print("Worked")
        count += 1
        output_file.write(name + '\n')

# Changing fie from appending to read and then printing line by line.
with open('names.txt', 'r') as output_file:
    contents = output_file.readlines()
for line in contents:
    print(line.strip())

# Q2, searching the list for item and option to add if not found.

search_list = []

with open('names.txt', 'r') as q2_file:
    contents_output = q2_file.readlines()
    for each_line in contents_output:
        search_list.append(each_line.strip('\n'))
    item = input("Search: ")
    if item in search_list:
        print(item, ' was found in the file.')
    else:
        print(item, ' was not found in the file.')
        option = input('Would you like to add it? y/n\n')
        if option == 'y':
            with open('names.txt', 'a+') as output_file:
                content_output = output_file.readlines()
                while len(item) < 10:
                    item = input("Name must be at least 10 characters, retry: ")
                print("Name added.")
                output_file.write(item + '\n')
                print(output_file.readlines())
        else:
            print('The name was not added nor found.')



# Q3
data_list = []
data_list_two = []
third_column_list = []
total_third = 0
with open('population2.txt', 'r') as data_file:
    content_output = data_file.readlines()
    print(content_output)

for item in content_output:
    new_list_item = item.strip('\n')
    data_list.append(new_list_item)

for item in data_list:
    new_list_item = item.split(' ')
    data_list_two.append(new_list_item)

for item in data_list_two:
    third_column = int(item[2])
    total_third += third_column
    third_column_list.append(third_column)

average = total_third / 10
print('Minimum age: ', min(third_column_list))
print('Maximum age: ', max(third_column_list))
print('Average age: ', round(average, 1))





















