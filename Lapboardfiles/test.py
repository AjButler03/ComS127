import re

# 11-29-2022
# testing for lapboard.py
# def create_categories():
#     cat_name_list = []
#     cat_name = input("Enter a lap category name: ")
#     while cat_name != "*":
#         cat_name_list.append(cat_name)
#         cat_name = input("Enter a lap category name (enter '*' to stop): ")
#     return cat_name_list
# def newlapboard():
#     lapBoard = {}
#     lapBoard["make"] = {}
#     lapBoard["model"] = {}
#     lapBoard["year"] = {}
#     lapBoard["time"] = {}
#     cat_name_list = create_categories()
#     for key in lapBoard:
#         for cat in cat_name_list:
#             lapBoard[key][cat] = ["1", "2", "3"]
#     return lapBoard
# def print_lapboard(lapBoard):
#     for cat in lapBoard["year"]:
#         print()
#         print(cat)
#         print()
#         for vehicle in range(0, len(lapBoard["year"][cat])):
#             print(lapBoard["year"][cat][vehicle] + " " + lapBoard["make"][cat][vehicle] + " " + lapBoard["model"][cat][vehicle] + ": " + lapBoard["time"][cat][vehicle])
# # board = newlapboard()
testboard = {'make': {'Muscle': ['Chevy', 'Dodge', 'Ford'], 'Supercar': ['Ferrari', 'lamborghini', 'Mclaren'], 'Compcat': ['Ford', 'Fiat', 'Mini']}, 'model': {'Muscle': ['Camaro', 'Viper', 'Mustang'], 'Supercar': ['F40', 'Huracan', 'Mp4-12c'], 'Compcat': ['Focus', 'Abarth', 'Cooper']}, 'year': {'Muscle': ['1969', '2013', '2005'], 'Supercar': ['1982', '2014', '2011'], 'Compcat': ['2014', '2010', '2012']}, 'time_formatted': {'Muscle': ['1:30', '2:30', '3:30'], 'Supercar': ['4:30', '5:30', '6:30'], 'Compcat': ['7:30', '8:30', '9:30']}}
# print_lapboard(testboard)

# 11-30-2022
# lapboard testing continued
# time_string = "1:53.238"
# converts a formatted lap time string (minutes:seconds.fractions) to a float representing seconds.
# def convert_to_seconds(time_string):
#     minutes_str = ""
#     seconds_str = ""
#     col_index = time_string.index(":")
#     for character in range(0, col_index):
#         minutes_str = minutes_str + time_string[character]
#     for character in range(col_index + 1, len(time_string)):
#         seconds_str = seconds_str + time_string[character]
#     minutes = float(minutes_str)
#     seconds = float(seconds_str) + minutes * 60
#     return seconds
# # converts a float representing seconds into a formatted time string (minutes:seconds.fractions)
# def format_time(seconds):
#     seconds_float = seconds % 60
#     minutes_int = int(seconds // 60)
#     formatted_time = str(minutes_int) + ":" + str(seconds_float)
#     return formatted_time
# seconds = convert_to_seconds(time_string)
# format_time(seconds)

# 12-2-2022

#this is code that is WIP to save/read a txt file of the lapboard. Complicated as fuck, moving on for now.

# def read_lapBoard_file(filename):
#     with open(filename + ".txt", "r") as f:
#         lines = f.readlines()
#         del lines[0]
#         for i in range(0, len(lines)):
#             lines[i] = lines[i].strip()
#             lines[i] = lines[i].split(";")
#         for i in range(0, len(lines)):
#             for j in range(0, len(lines[i])):
#                 lines[i][j] = lines[i][j].split()
#         print(lines)
# def write_lapBoard_file(lapBoard, filename):
#     with open(filename + ".txt", "w") as f:
#         f.write("File: " + filename + "\n")
#         for cat in lapBoard["year"]:
#             f.write(cat +"\n")
#             for j in range(0, len(lapBoard["year"][cat])):
#                 # not sure how to find the last iteration of a dictionary (I realize that there is technically no set order to keys in a dict, it iterates through in the order it's written), so the file will just have an extra line at the end.
#                 # After looking, there are both ways to remove the last character and to find the last iteration of a dict, but I don't understand how either works. So we'll just go with this.
#                 f.write(lapBoard["year"][cat][j] + " " + lapBoard["make"][cat][j] + " " + lapBoard["model"][cat][j] + "; " + lapBoard["time_formatted"][cat][j] + "\n")
# filename = "test_file"
# read_lapBoard_file(filename)
# write_lapBoard_file(testboard, filename)


# 12-03-2022
# vehicle_list = [['1969', 'chevrolet', 'camaro'], ['1969', 'ford', 'mustang'], ['2014', 'lamboghini', 'huracan']]
# time_list = ['2:30.123', '3:30.567', '87:46.108']

# def print_lapboard(vehicle_list, formatted_time_list):
#     for i in range(0, len(vehicle_list)):
#         for j in range(0, len(vehicle_list[i])):
#             print(vehicle_list[i][j], end="")
#             if j < len(vehicle_list[i])-1:
#                 print(" ", end="")
#             else:
#                 print("; ", end="")
#         print(formatted_time_list[i])
# print_lapboard(vehicle_list, time_list)

# takes in a filename (without .txt) and gathers the formatted lap times and vehicles from it. Returns vehicle_list and times_list.
def loadBoard(filename):
    with open(filename + ".txt", "r") as f:
        lines = f.readlines()
        time_list = []
        vehicle_list = []
        for i in range(0, len(lines)):
            lines[i] = lines[i].strip()
            lines[i] = lines[i].split(";")
            for j in range(0, len(lines[i])):
                lines[i][j] = lines[i][j].strip()
                lines[i][j] = lines[i][j].split(" ", 2)
            vehicle_list.append(lines[i][0])
            time_list.append(lines[i][1][0])
            del lines[i][1]
    return vehicle_list, time_list

# takes in a filename (without .txt), vehicle_list, and times_list. Writes out the information into a lapboard format as a txt file.
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

vehicle_list, time_list = loadBoard("testboard")
saveBoard("testboard2", vehicle_list, time_list)