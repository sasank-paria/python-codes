
dictionary = { "shashank":"to be a billionaire",
              "charecter":"hardworking guy",
              "age":20 ,
              "listof number":[10,15,58]
}

print(dictionary.keys())
print(dictionary.values())
print(dictionary["shashank"])
print(dictionary["listof number"])

dictionaryupdate={"shashank":"to be a trillionaire"}

dictionary.update(dictionaryupdate)

print(dictionary.items())

dictionary["listof number"]=[5,2,8,7,4]

print(dictionary.items())

print(dictionary.get("shashank"))