# Andrew Butler             10-24-2022
# Dictionaries demo

# dictionaries are similar to lists, but the information contained inside is accessed by keys instead of indexes; basically the index is whatever the fuck you want it to be

# testDict = {}
# testDict["apple"] = "red"
# testDict[2] = "Two"
# testDict[1.3] = "one point three"
# print(testDict)
# print(testDict["apple"])


# foodList = {}
# foodList["Breakfast"] = []
# foodList["Dinner"] = []
# foodList["Breakfast"].append("banana")
# foodList["Breakfast"].append("apples")
# foodList["Dinner"].append("chicken")
# foodList["Dinner"].append("Tacos")
# print(foodList)
# print(foodList["Breakfast"])
# print(foodList["Breakfast"][0])


# d1 = {"one" : 1, "two" : 2}
# d2 = {"two" : 2, "one" : 1}
# print(d1)
# print(d2)
# print(d1 == d2)


#keys method
testDict = {"one" : 1, "two" : 2, "three" : 3}
keys = testDict.keys()
print(keys)
# this works
for key in keys:
    print(testDict[key])
# this does not
# print(keys[0])


# testDict = {"one" : 1, "two" : 2, "three" : 3}
# print("one" in testDict)
# print("one" in testDict.keys())
# print(1 in testDict)

# Values method; same as keys method, but with values
# testDict = {"one" : 1, "two" : 2, "three" : 3}
# print(1 in testDict)
# print("one" in testDict.values())
# print(1 in testDict.values())


#items method
# testDict = {"one" : 1, "two" : 2, "three" : 3}
# dict_items = testDict.items()
# print(dict_items)
# for k, v in dict_items:
#     print(k, v)


# Get method
# carsdict = {"Subaru" : "blue", "Buick" : "silver", "porshe" : "black"}
# print(carsdict)
# print(carsdict.get("Subaru", 0))
# print(carsdict.get("Chevrolet", 0))
# print(carsdict)

