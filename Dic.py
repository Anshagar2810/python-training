#Write a python program to create and print a dictionary which stores your information.(name, age, gender .....)
print("Question 1")
print("Answer")

info = {
    "name": "Ansh Agarwal",
    "age": 18,
    "gender": "Male"
}

print(info)

#. Write a python program to access the items of a dictionary by referring to its key name.
print("\nQuestion 2")
print("Answer")

info = {
    "name": "Ansh Agarwal",
    "age": 18,
    "gender": "Male"
}

print(info["name"])

#Write a python program to get a list of the values from a dictionary.
print("\nQuestion 3")
print("Answer")

info = {
    "name": "Ansh Agarwal",
    "age": 18,
    "gender": "Male"
}

print(list(info.values()))

#Write a python program to change the value of a specific item by referring to its key name.
print("\nQuestion 4")
print("Answer")

info = {
    "name": "Ansh Agarwal",
    "age": 18,
    "gender": "Male"
}

info["age"] = 19
print(info)

#Write a python program to print all key names in the dictionary, one by one.
print("\nQuestion 5")
print("Answer")

info = {
    "name": "Ansh Agarwal",
    "age": 18,
    "gender": "Male"
}

for key in info:
    print(key)

#Write a python program to create a dictionary that contains three dictionaries. (nested)
    print("\nQuestion 6")
print("Answer")

student = {
    "student1": {"name": "Aman", "age": 18},
    "student2": {"name": "Riya", "age": 19},
    "student3": {"name": "Ansh", "age": 18}
}

print(student)

#Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
print("\nQuestion 7")
print("Answer")

d1 = {"name": "Ansh"}
d2 = {"age": 18}
d3 = {"gender": "Male"}

combined = {
    "dict1": d1,
    "dict2": d2,
    "dict3": d3
}

print(combined)

#Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
print("\nQuestion 8")
print("Answer")

list1 = ["name", "age", "gender"]
list2 = ["Ansh", 18, "Male"]

result = dict(zip(list1, list2))
print(result)

#Write a python program to merge two python dictionaries into one dictionary.
print("\nQuestion 9")
print("Answer")

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict1.update(dict2)
print(dict1)

#Write a python program to get the key of lowest value from the dictionary. sample
#dict = {
#'C': 92,
#'Java': 66,
#'Python': 85
#}
print("\nQuestion 10")
print("Answer")

marks = {
    "C": 92,
    "Java": 66,
    "Python": 85
}

print(min(marks, key=marks.get))


