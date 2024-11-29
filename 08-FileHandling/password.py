import re

# read username and password from keyboard
username = input("Input username: ")
password = input("Input password: ")

# pattern (criteria) for username and password
username_pattern = '/[a-z]{6, 100}'
password_pattern = '\w{8, 100}'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)
print(username_match)
# print results
# if ... and ...:
#    print(...)
# else:
#    ... 