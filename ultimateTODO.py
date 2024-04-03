# Andrew Butler             11-1-2022
# Assignment #5

import sys
import pickle

def initList():
    todoList = {}
    todoList["backlog"] = []
    todoList["todo"] = []
    todoList["in_progress"] = []
    todoList["in_review"] = []
    todoList["done"] = []

    return todoList

# Does a saving thing
def saveList(todoList):
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "wb") as pickle_file:
            pickle.dump(todoList, pickle_file)
    except:
        print("ERROR (saveList): ./{0}.lst is not a valid file name!".format(listName))
        sys.exit()

# Does a loading thing
def loadList():
    try:
        listName = input("Enter List Name (Exclude .lst Extension): ")
        with open("./" + listName + ".lst", "rb") as pickle_file:
            todoList = pickle.load(pickle_file)
    except:
        print("ERROR (loadList): ./{0}.lst was not found!".format(listName))
        sys.exit()
    
    return todoList

# Takes in a todoList (in form of dictionary of lists) and a specified item to look for, and returns whether that item was found in the dictionary and the key/index where it was found, if it was found.
def checkItem(item, todoList):
    itemFound = False
    keyName = ""
    index = -1
    for key in todoList:
        if item in todoList[key]:
            keyName = key
            index = todoList[key].index(item)
            itemFound = True
    return itemFound, keyName, index

# takes in a specified item, the key of the list it should go into, and the dictionary of lists that list is located in. Appends item to specified list if that item does not already exist in dictionary, and returns modified todoList dictionary.
def addItem(item, toList, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound == False:
        todoList[toList].append(item)
    else:
        print("Item {0} already in list {1} at index {2}".format(item, keyName, index))
    return todoList

# takes in specified item, and the todoList dictionary. Finds and deletes item, returns modified todoList dictionary. Also returns the boolean value for whether the item was found in the dictionary or not.
def deleteItem(item, todoList):
    itemFound, keyName, index = checkItem(item, todoList)
    if itemFound == True:
        del todoList[keyName][index]
    else:
        print("Error: item {0} is not in the todo list".format(item))
    return itemFound, todoList

def moveItem(item, toList, todoList):
    itemFound, todoList = deleteItem(item, todoList)
    if itemFound == True:
       todoList = addItem(item, toList, todoList)
    return todoList

# takes in the todoList dictionary and prints out the key of the list and the list itself. Does not return anything.
def printTODOList(todoList):
    for key in todoList:
        print(key + ":", end = "")
        print(todoList[key])
    return None

def runApplication(todoList):
    while True:
        print("-----------------------------------------------------------------")
        choice = input("APPLICATION MENU: [a]dd to backlog, [m]ove item, [d]elete item, [s]ave list, or [q]uit to main menu?: ")
        print()

        if choice == "a":

            # code to add item to any keylist, instead of just backlog.
            # toList = str(input("Add to \"backlog\", \"todo\",  \"in_progress\", \"in_review\", or \"done\"?: "))
            # while toList != "backlog" and toList != "todo" and toList != "in_progress" and toList != "in_review" and toList != "done":
            #     print("Error: {0} key does not exist. Please enter \"backlog\", \"todo\",  \"in_progress\", \"in_review\", or \"done\".")
            #     toList = str(input("Add to \"backlog\", \"todo\",  \"in_progress\", \"in_review\", or \"done\"?: "))

            item = str(input("Enter an item: "))
            todoList = addItem(item, "backlog", todoList)
            print()
            printTODOList(todoList)

        elif choice == "m":

            if todoList["backlog"] == [] and todoList["todo"] == [] and todoList["in_progress"] == [] and todoList["in_review"] == [] and todoList["done"] == []:
                print("Error: No items to move")
            else:
                item = str(input("Enter the item you'd like to move: "))
                itemFound, keyName, index = checkItem(item, todoList)
                while itemFound != True:
                    item = str(input("Error: Item not found. Enter a different item to move: "))
                    itemFound, keyName, index = checkItem(item, todoList)
                toList = str(input("Move to \"backlog\", \"todo\",  \"in_progress\", \"in_review\", or \"done\"?: "))
                while toList != "backlog" and toList != "todo" and toList != "in_progress" and toList != "in_review" and toList != "done":
                    print("Error: {0} key does not exist. Please enter \"backlog\", \"todo\",  \"in_progress\", \"in_review\", or \"done\".")
                    print()
                    toList = str(input("Move to \"backlog\", \"todo\",  \"in_progress\", \"in_review\", or \"done\"?: "))
                todoList = moveItem(item, toList, todoList)
            printTODOList(todoList)

        elif choice == "d":
            item = str(input("Enter the item you'd like to delete: "))
            itemFound, keyName, index = checkItem(item, todoList)
            while itemFound != True:
                item = str(input("Error: Item not found. Enter a different item to delete: "))
                itemFound, keyName, index = checkItem(item, todoList)
            itemFound, todoList = deleteItem(item, todoList)
            print()
            printTODOList(todoList)

        elif choice == "s":

            saveList(todoList)
            print("Saving List...")
            print()
            printTODOList(todoList)
            
        elif choice == "q":

            print("Returning to MAIN MENU...")
            print()
            break
        else:
            print("ERROR: Please enter [a], [m], [d], [s], or [q].")
            print()

    return todoList

def main():
    taskOver = False

    print("The Ultimate TODO List")
    print()
    
    print("By: Andrew Butler")
    print("[COM S 127 B]")
    print()

    while taskOver == False:
        print("-----------------------------------------------------------------")
        choice = input("MAIN MENU: [n]ew list, [l]oad list, or [q]uit?: ")
        print()
        if choice == "n": 
            todoList = initList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "l":
            todoList = loadList()

            printTODOList(todoList)
            
            runApplication(todoList)
        elif choice == "q":
            taskOver = True
            print("Goodbye!")
            print()
        else:
            print("Please enter [n], [l], or [q]...")
            print()

if __name__ == "__main__":
    main()