import re # module for regular expressions
email_file = 'report.txt'
def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content
email = read_from_file(email_file)

# regular expression pattern
# for amounts
pattern = '\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
total = 0
for amount in amounts:
   total += int(amount)

# print result
print(total)