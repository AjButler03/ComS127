# Andrew Butler             12-03-2022
# Lap Board App

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# This is a lapboard app; the intention is to be able to create, load, edit, and save a series of ordered lap times for various vehicles. In effect, this script functions fairly similarly to ultimateTODO.

# This script primarily focuses on manipulating three lists; Vehicle_list, time_list, and time_seconds_list. These are meant to be parallel to one another. For example, index 0 for each is information about the same vehicle.
# The user initially has 3 options in the first program loop (main function); create a new lap board, load a lapboard, or quit. Quit does what you'd expect.
# Creating a new lapboard intitiates the three lists I talked about above, and runs the second program loop (run function); more about that in a second.
# Loading a new list will prompt the user for a filename, and then it will open, read, and pull information to populate vehicle_list, time_list, and time_seconds_list. The user then has the options for the second program loop (run function).

# whithin the second loop, the user has the option to add, edit, or delete a specific vehicle's time, as well as the option to save the lap board and to quit back to the first program loop.
    # adding a time takes input for the year, make, and model of the vehicle, and appends this as a list within the vehicle_list list. The user will also be prompted for a lap time, which they enter as XX:XX.xxx (for example, 1:47.246).
        # lots of stuff happens with that inputted time. First it's appended to time_list, then it's converted from a string to a float representing seconds and appended to time_seconds_list. From there, the insertion sort algorithm is
        # used to sort vehicle_list, time_list, and time_seconds_list based on which time is the fastest whithin time_seconds_list. This makes it so that when the lap board is printed or saved, the fastest time is always at the top, 
        # decending in order from there.
    # deleting a time will take input for year, make, and model, then delete that list from vehicle_list, as well as the matching indexes from time_list and time_seconds_list.
    # editing a time will first go through the process of deleting that time, then adding it with a new input for time_list. 
    # saving a lapboard will take input for what the filename they want to save to is, and then write out a .txt file with that name using the information contained within vehicle_list and time_list.
        # this will be written line by line, with each line being in the format "year make model; XX:XX.xxx"
    # quit will send the user back to the first program loop.

# there are checks to make sure inputs are valid, and error messages will print if they are not. There are a couple instances of using a try/except statement for running a function, which I realize is probably not the best way to go about things, but it works.
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# declares vehicle_list, time_list, and time_seconds_list. Returns those three lists.
def new_lapBoard():
    vehicle_list = []
    time_list = []
    time_list_seconds = []
    return vehicle_list, time_list, time_list_seconds

# converts a formatted lap time string (minutes:seconds.fractions) to a float representing seconds.
def convert_to_seconds(time_string):
    minutes_str = ""
    seconds_str = ""
    col_index = time_string.index(":")
    for character in range(0, col_index):
        minutes_str = minutes_str + time_string[character]
    for character in range(col_index + 1, len(time_string)):
        seconds_str = seconds_str + time_string[character]
    minutes = float(minutes_str)
    seconds = float(seconds_str) + minutes * 60
    return seconds

# converts a float representing seconds into a formatted time string (minutes:seconds.fractions).
def format_time(seconds):
    seconds_float = round((seconds % 60), 3)
    if seconds_float < 10:
            seconds_str = "0" + str(seconds_float)
    else:
        seconds_str = str(seconds_float)
    minutes_int = int(seconds // 60)
    formatted_time = str(minutes_int) + ":" + seconds_str
    return formatted_time

# takes input to get year, make, and model of the vehicle. Returns year, make, model in the form of a list.
def specify_vehicle():
    year = input("Enter the model year: ")
    make = input("Enter the manufacturer: ")
    model = input("Enter the model: ")
    vehicle = []
    vehicle.append(year)
    vehicle.append(make)
    vehicle.append(model)
    return vehicle

# checks to see if a specified vehicle (list of year, make, model) is already listed in vehicle_list, and returns a boolean value of if it was found and the index if it was.
def check_vehicle(vehicle, vehicle_list):
    itemFound = False
    index = -1
    if vehicle in vehicle_list:
        index = vehicle_list.index(vehicle)
        itemFound = True
    return itemFound, index

# input vehicle_list and time_list; using insertion sorting, sort the times from fastest (least # of seconds) to slowest (most # of seconds), and sorting vehicle_list and time_list (str formatted times) to match. Returns modified vehicle_list and time_list.
def sort_times(vehicle_list, time_list, time_list_seconds):
    for step in range(1, len(time_list_seconds)):
        key = time_list_seconds[step]
        key2 = vehicle_list[step]
        key3 = time_list[step]
        j = step -1
		   
        while j >= 0 and key < time_list_seconds[j]:
            time_list_seconds[j + 1] = time_list_seconds[j]
            vehicle_list[j + 1] = vehicle_list[j]
            time_list[j + 1] = time_list[j]
            j = j -1

            time_list_seconds[j + 1] = key
            vehicle_list[j + 1] = key2
            time_list[j + 1] = key3
    return vehicle_list, time_list, time_list_seconds

# takes in input for a new lap time (str in form XX:XX.xxx) appends it to time_list, and appends a version of it converted to seconds to time_list_seconds. Vehicle_list, time_list, and time_seconds_list are all then sorted by time. Modified vehicle_list, time_list, and time_seconds_list are returned.
def add_time(vehicle_list, time_list, time_list_seconds):
    while True:
        time = input("Enter the lap time (XX:XX.XXX): ")
        # I know that its probably not best practice, but it should check to make sure that the entered time can actually be parsed by my conversion function. If an error occures, the user will be asked to enter a valid time.
        try:
            time_seconds = convert_to_seconds(time)
            time_list_seconds.append(time_seconds)
            break
        except:
            print("Error: invalid time format. please enter time in XX:XX.xxx format")
    # converting to number then back to string makes it so if the user inputs a time like "1:24324.234" there will only be two digits for seconds on the actual lapboard.
    time_list.append(format_time(time_seconds))
    vehicle_list, time_list, time_list_seconds = sort_times(vehicle_list, time_list, time_list_seconds)
    return vehicle_list, time_list, time_list_seconds

# takes in the lists vehicle, vehicle_list, time_list, time_seconds_list
# checks to see if vehicle is in vehicle_list, and deletes it if it is. Deletes same index in time_list, time_seconds list.
def delete_vehicle_time(vehicle, vehicle_list, time_list, time_seconds_list):
    itemFound, index = check_vehicle(vehicle, vehicle_list)
    if itemFound == True:
        del vehicle_list[index]
        del time_list[index]
        del time_seconds_list[index]
    else:
        print("Error: vehicle not found.")
    return itemFound, vehicle_list, time_list, time_seconds_list

# takes in lists vehicle, vehicle_list, time_list, time_list_seconds. Checks to see if vehicle exists whithin vehicle_list, and appends it if it doesn't.
# if vehicle is not found within vehicle list, add_time() function runs, appending a time in seconds to time_list_seconds and a formatted time string to time_list.
# returns modified vehicle_list, time_list, and time_list_seconds.
def add_vehicle(vehicle, vehicle_list, time_list, time_list_seconds):
    itemFound, index = check_vehicle(vehicle, vehicle_list)
    if itemFound == False:
        vehicle_list.append(vehicle)
        vehicle_list, time_list, time_list_seconds = add_time(vehicle_list, time_list, time_list_seconds)
    else:
        print("Error: vehicle already on lapboard")
    return vehicle_list, time_list, time_list_seconds

# takes in lists vehicle, vehicle_list, time_list, time_list_seconds. checks to see if vehicle exists whithin vehicle_list, and deletes it and the corresponding indicies from time_list and time_list_seconds if it does.
# assuming vehicle was found and deleted, vehicle and it's new time is appended and sorted to vehicle_list, time_list, and time_seconds_list.
# returns modified vehicle_list, time_list, and time_list_seconds.
def edit_vehicle_time(vehicle, vehicle_list, time_list, time_list_seconds):
    itemFound, vehicle_list, time_list, time_seconds_list = delete_vehicle_time(vehicle, vehicle_list, time_list, time_list_seconds)
    if itemFound == True:
        vehicle_list, time_list, time_list_seconds = add_vehicle(vehicle, vehicle_list, time_list, time_list_seconds)
    return vehicle_list, time_list, time_list_seconds

# takes in vehicle_list (list of lists of strings) and time_list (list of strings). prints out the information strings in each list within vehicle_list and oresponding time for the index of that list on individual lines.
def print_lapboard(vehicle_list, time_list):
    print()
    for i in range(0, len(vehicle_list)):
        for j in range(0, len(vehicle_list[i])):
            print(vehicle_list[i][j], end="")
            if j < len(vehicle_list[i])-1:
                print(" ", end="")
            else:
                print("; ", end="")
        print(time_list[i])
    print()

# takes in a filename (without .txt) and gathers the formatted lap times and vehicles from it. Returns vehicle_list and times_list.
def loadBoard(filename):
    with open(filename + ".txt", "r") as f:
        lines = f.readlines()
        time_list = []
        vehicle_list = []
        time_seconds_list = []
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip()
            lines[i] = lines[i].split(";")
            for j in range(0, len(lines[i])):
                lines[i][j] = lines[i][j].strip()
                lines[i][j] = lines[i][j].split(" ", 2)
            vehicle_list.append(lines[i][0])
            time_list.append(lines[i][1][0])
            del lines[i][1]
        for i in range(0, len(time_list)):
            time_seconds = convert_to_seconds(time_list[i])
            time_seconds_list.append(time_seconds)
    return vehicle_list, time_list, time_seconds_list

# takes in a filename (without .txt), vehicle_list, and times_list. Writes out the information line by line with year, make, model, and formatted lap time.
def saveBoard(filename, vehicle_list, time_list):
    with open(filename + ".txt", "w") as f:
        for i in range(0, len(vehicle_list)):
            for j in range(0, len(vehicle_list[i])):
                f.write(vehicle_list[i][j])
                if j < len(vehicle_list[i])-1:
                    f.write(" ")
            f.write("; " + time_list[i])
            if i < len(vehicle_list)-1:
                f.write("\n")

# primary code loop for looking at the lapboard; takes input for what the user wants to do, and runs appropriate functions to achieve that.
def run(vehicle_list, time_list, time_list_seconds):
    while True:

        if vehicle_list == []:
            print()
            print("EMPTY LAP BOARD")
            print()
        else:
            print_lapboard(vehicle_list, time_list)
        choice = input("MENU: [a]dd time, [e]dit time, [d]elete time, [s]ave lap board, or [q]uit to main menu?: ")

        if choice == "a":

            vehicle = specify_vehicle()
            vehicle_list, time_list, time_list_seconds = add_vehicle(vehicle, vehicle_list, time_list, time_list_seconds)

        elif choice == "e":
            if vehicle_list == []:
                print("Error: there are no times to edit.")
            else:  
                vehicle = specify_vehicle()
                itemFound, index = check_vehicle(vehicle, vehicle_list)
                if itemFound == True:
                    vehicle_list, time_list, time_list_seconds = edit_vehicle_time(vehicle, vehicle_list, time_list, time_list_seconds)
                else:
                    print("Error: specified vehicle is not on the lap board")
                
        elif choice == "d":
            vehicle = specify_vehicle()
            itemFound, index = check_vehicle(vehicle, vehicle_list)
            if itemFound == True:
                itemFound, vehicle_list, time_list, time_list_seconds = delete_vehicle_time(vehicle, vehicle_list, time_list, time_list_seconds)
            else:
                print("Error: specified vehicle is not on the lap board")

        elif choice == "s":
            filename = input("Enter the filename to save to (without .txt): ")
            print("Saving lap board to {0}.txt.... ", end = "".format(filename))
            saveBoard(filename, vehicle_list, time_list)
            print("done")
        elif choice == "q":
            print("Returning to main menu...")
            print()
            break
        else:
            print("Error: please enter [a], [e], [d], [s], or [q].")

# main does the main thing here
def main():
    quit = False

    print("Lap Board App")
    print()
    
    print("By: Andrew Butler")
    print("[COM S 127 B]")
    print()

    while quit == False:
        print("----------------------------Welcome----------------------------")
        choice = input("[n]ew lap board, [l]oad lap board, or [q]uit?: ")
        if choice == "n":
            vehicle_list, time_list, time_seconds_list = new_lapBoard()
            run(vehicle_list, time_list, time_seconds_list)

        elif choice == "l":
            filename = input("Enter the filename (without .txt) to load: ")
            # I know that its probably not best practice, but this try statement will ensure that an improperly formatted file or a invalid file name won't cause errors.
            try:
                vehicle_list, time_list, time_seconds_list = loadBoard(filename)
                run(vehicle_list, time_list, time_seconds_list)
            except:
                print("Error: invalid file or file name")

        elif choice == "q":
            print("----------------------------Goodbye----------------------------")
            print()
            quit = True
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()