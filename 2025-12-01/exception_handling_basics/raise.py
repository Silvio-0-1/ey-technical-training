def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")
    return "Allowed"

print (check_age(20))
# print(check_age(15)) # triggers exception