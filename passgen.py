import random
import string
length = int(input("Enter the length you want your password to be :"))
password = ""
lower = string.ascii_lowercase + string.digits
upper_lower = string.ascii_letters  + string.digits
special = string.punctuation + string.digits
all = string.ascii_letters + string.digits + string.punctuation

upper_or_not = input("Do you want uppercase characters or not ?(yes/no):")
special_characters_or_not = input("Do you want special characters or not ?(yes/no):")

if upper_or_not == "yes" and special_characters_or_not == "no":
    for l in range(length):
        password += random.choice(upper_lower)
    print("Your password is : %s " % password)

elif upper_or_not == "yes" and special_characters_or_not == "yes":
    for l in range(length):
        password += random.choice(all)
    print("Your password is : %s " % password)
    
elif upper_or_not == "no" and special_characters_or_not == "no":
    for l in range(length):
        password += random.choice(lower)
    print("Your password is : %s" % password)
    
else:
    print("Error you must enter yes or no anything else and it won't work .")
    
