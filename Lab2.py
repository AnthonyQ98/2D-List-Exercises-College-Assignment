"""
Anthony Quinn X00138635
08/02/2021
Lab 2 Exercises
"""
import time

weekly_target = float(input("Weekly Target: "))

salespeople_list = []
sales_weekly = []
counter = 0
total_overall = 0
exceeded_list = []
exceeded = 0
all_targets = []

for person in range(2):
    day_counter = 0
    total_weekly = 0
    individual_target = float(input("Individual Weekly Target for Salesperson {}: ".format(counter + 1)))
    for day in range(5):
        sales_per_day = float(input("Salesperson {}, Day {} sales: ".format(counter + 1, day_counter + 1)))
        day_counter += 1
        total_weekly += sales_per_day
        total_overall += sales_per_day
    all_targets.append(individual_target)
    sales_weekly.append(total_weekly)
    counter += 1
print("-" * 65)

for i, item in enumerate(sales_weekly):
    print("Salesperson {0}\t\t\t Weekly Sales: {1}".format(i+1, item))

for i, item in enumerate(sales_weekly):
    amount_exceeded = 0
    if item > weekly_target:
        exceeded += 1
        amount_exceeded = item - weekly_target
        exceeded_list.append(amount_exceeded)
        print("Salesperson ", i+1, " exceeded the weekly target by ", amount_exceeded)


print("-" * 65)
print("Total sales for the week:     ", total_overall)
if exceeded != 0:
    print("Salespeople Exceeded Target: ", exceeded)
else:
    print("0 salespeople exceeded the weekly target!")

# Version 2 comparing
print("-" * 65)
for i in range(len(all_targets)):
    if sales_weekly[i] > all_targets[i]:
        individual_exceeded = sales_weekly[i] - all_targets[i]
        print("Salesperson ", i+1, " exceeded their individual target by ", individual_exceeded)

time_string = time.strftime("%d/%m/%Y, %H:%M:%S")


text_file = open("output.txt", "a")
text_file.write("\n")
text_file.write("-" * 65)
text_file.write("\nTime and Date: {}".format(time_string))
text_file.write("\nExceeded weekly target: {} salespeople.".format(exceeded))
text_file.write("\nSales Weekly: {}".format(sales_weekly))
text_file.close()
