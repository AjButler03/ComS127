# Andrew Butler             12-09-2022
# lap Board app

# creates a list of strings from user input to be used as keys in a dictionary. Returns created list.
def create_categories():
    cat_name_list = []
    cat_name = input("Enter a lap category name: ")
    while cat_name != "*":
        cat_name_list.append(cat_name)
        cat_name = input("Enter a lap category name (enter '*' to stop): ")
    return cat_name_list

# creates a dictionary of dictionaries of lists- the lap board that the user will see. 
# The outer dictionary has keys for the make, model, year, lap time in seconds (float) and formatted lap time (string) for the specified vehicle
# the inner dictionaries use keys created by the create_categories function, and contain lists for each.
# the newlapboard function returns the lap board dictionary.
def newlapboard():
    lapBoard = {}
    lapBoard["make"] = {}
    lapBoard["model"] = {}
    lapBoard["year"] = {}
    lapBoard["time_seconds"] = {}
    lapBoard["time_formatted"] = {}
    cat_name_list = create_categories()
    for key in lapBoard:
        for cat in cat_name_list:
            lapBoard[key][cat] = []
    return lapBoard

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
    seconds_float = seconds % 60
    minutes_int = int(seconds // 60)
    formatted_time = str(minutes_int) + ":" + str(seconds_float)
    return formatted_time

# takes in an item and the lapBoard dict. Checks to see if the specified item is in the dict anywhere, and returns the keys for the outer and inner dict, as well as the index where it is located.
def checkItem(item, lapBoard):
    itemFound = False
    keyname1 = ""
    keyname2 = ""
    index = -1
    for key1 in lapBoard:
        for key2 in lapBoard[key1]:
            if item in lapBoard[key1][key2]:
                keyname1 = key1
                keyname2 = key2
                index = lapBoard[key1][key2].index(item)
                itemFound = True
    return itemFound, keyname1, keyname2, index

def addItem(item, datatype, cat, toList, todoList):
    itemFound = False
    # Only checking make and model here, since those are the only things to be unique.
    if datatype == "make" or datatype == "model"
        itemFound, keyname1, keyname2, index = checkItem(item, todoList)
    if itemFound == False:
        lapBoard[datatype][cat].append(item)
    else:
        print("Item {0} already in {1} category at index {2}".format(item, keyname2, index))
    return todoList

# prints out the lapboard by category; for example, it wil print the year, make, model, and formatted time for each vehicle in a category called "muscle", then the same for the next category.
def print_lapboard(lapBoard):
    for cat in lapBoard["year"]:
        print()
        print(cat)
        for vehicle in lapBoard["year"][cat]:
            print(lapBoard["year"][cat][vehicle] + " " + lapBoard["make"][cat][vehicle] + " " + lapBoard["model"][cat][vehicle] + "; " + lapBoard["time_formatted"][cat][vehicle])

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
            lapBoard = newlapboard()
            print_lapboard(lapBoard)
        elif choice == "l":
            pass
        elif choice == "q":
            quit = True
            print("----------------------------Goodbye----------------------------")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()