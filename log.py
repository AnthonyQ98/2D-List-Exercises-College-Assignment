import time

time_string = time.strftime("%d/%m/%Y, %H:%M:%S")
option = 0

while option != 3:
    print("*****************")
    print("* Log System    *")
    print("* 1) Log System *")
    print("* 2) Print Logs *")
    print("* 3) Exit       *")
    option = int(input("Select an option (1 - 3): "))

    if option == 1:
        file_open = open("log.txt", "a")
        user_message = input("Enter your log message: ")
        file_open.write("Log Date & Time: {}\n".format(time_string))
        file_open.write("{}\n".format(user_message))
        file_open.close()
    elif option == 2:
        file_open = open("log.txt", "r")
        store_read = file_open.read()
        print(store_read)
        file_open.close()
    elif option == 3:
        print("Exit selected. Program finished.")
    else:
        print("Invalid option selected, try again!")
