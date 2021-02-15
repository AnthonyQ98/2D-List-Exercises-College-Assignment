student_tests = []
students_amount = 5
amount_individual_tests = 4
total = 0
total_tests = 0
above_average_counter = 0

# q1
for student in range(students_amount):
    temp_list = []
    for test in range(amount_individual_tests):
        mark = float(input("Student {}, Test {}: ".format(student + 1, test + 1)))
        if mark >= 0 and mark <= 100:
            total += mark
        while mark < 0 or mark > 100:
            mark = float(input("Enter mark between 0 and 100: "))
            if mark >= 0 and mark <= 100:
                total += mark
        total_tests += 1
        temp_list.append(mark)
    student_tests.append(temp_list)
    print(total)

# q2
average_of_all_tests = total / total_tests
print("Average of all tests: ", average_of_all_tests)

# q3
for i, student in enumerate(student_tests):
    total_student = 0
    for item in student:
        total_student += item
    average_student = total_student / amount_individual_tests
    difference = average_student - average_of_all_tests
    print("Average for student {}: ".format(i + 1), average_student)
    print("Difference between student {} average and overall average: ".format(i + 1), round(difference, 2))
    if average_student >= average_of_all_tests:
        print("Congratulations, you were equal or above average overall!")
        above_average_counter += 1
    else:
        print("You scored below the overall average!")
# Q4
print("Number of students who scored above or equal to average: ", above_average_counter)

# Q5
temp_list = []
for i, item in enumerate(student_tests):
    temp_list.append(max(item))

max_result_name_student = temp_list.index(max(temp_list))
print("Max result scored by student {}, their result was: ".format(max_result_name_student + 1), max(temp_list))

# Q6
total_each_student = []
for i, student in enumerate(student_tests):
    total_student = 0
    for item in student:
        total_student += item
    total_each_student.append(total_student)

# Q7
lowest_total_mark_student = total_each_student.index(min(total_each_student))
print("Lowest total mark scored by student {}, their total was: ".format(lowest_total_mark_student + 1), min(total_each_student))

# Q8
print(sorted(total_each_student))




