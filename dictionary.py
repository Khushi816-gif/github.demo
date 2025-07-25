#dictionary
#how to create a dictonary:
my_dict = {
    "name" : "khushi" , "age" : 21 , "marks" : (75.2,50,90,80) , 100 : "abc"
}
print(my_dict)

#concatenation
dict = {
    "fruits":("banana","apple"), "category" : "fruits"
}
print(dict)
dict["price"] = 100
print(dict)

#updating
dict = {
    "fruits":("banana","apple"), "category" : "fruits"
}
dict["category"] = "healthy fruits"
print(dict)

#delete
dict = {
    "fruits":("banana","apple"), "category" : "fruits"
}
del dict["category"] 
print(dict)

#methods in dictionary
#get()
profile = {
    "name":"khushi","age":21,"salary":35000.00
}

age = profile.get("age")
print(age)
#if it doesnt exists the type not found beside
age = profile.get("age_2","not found")
print(age)

#keys()
profile = {
    "name":"khushi","age":21,"salary":35000.00
}

keys = profile.keys()
print(keys)

#values
profile = {
    "name":"khushi","age":21,"salary":35000.00
}

values = profile.values()
print(values)

#items
profile = {
    "name":"khushi","age":21,"salary":35000.00
}

all_items = profile.items()
print(list(all_items))

#pop 
profile = {
    "name":"khushi","age":21,"salary":35000.00
}

popped = profile.pop("age")
print(popped)
print(profile)

popped = profile.pop("age_2","not found")
print(popped)
print(profile)

#popitem
profile = {
    "name":"khushi","age":21,"salary":35000.00
}

popped = profile.popitem()
print(popped)
print(profile)

#clear
profile = {
    "name":"khushi","age":21,"salary":35000.00
}

clear = profile.clear()
print(clear)
print(profile)

#dictonary comprhension
squares = {i : i**2 for i in range(1,11)}
print(squares)

#nested dictionary
programming_languages = {
    "python" : {"name":"python","usecase":["aiml,ds"]},
    "java" : {"name":"java","usecase":["aiml,ds"]},
}
print(programming_languages)

#loops in dictonary

profile = {
    "name":"khushi","age":21,"salary":35000.00
}
for keys in profile:
    print(keys)

#if we want values
profile = {
    "name":"khushi","age":21,"salary":35000.00
}
for keys in profile.values():
    print(keys)

#if we want items
profile = {
    "name":"khushi","age":21,"salary":35000.00
}
for keys in profile.items():
    print(keys)


