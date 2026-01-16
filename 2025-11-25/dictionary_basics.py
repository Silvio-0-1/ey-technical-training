student = {
"name" : "Abdullah",
"age" : 35,
"city : "Hyderabad"
}

print(student["name"])
print(student["age"])
print(student.get("email"))

# or 

print(student.get("name"))

student["email"] = "test@example.com"
student ["city"] = "Dubai"


student.pop("age") # remove by key
del student["city"] # delete
student.clear() # empty dictionary
