def read_from_file(name):
   with open(name) as file:
      content = file.read()
   return content
file_content = read_from_file('it_company.csv')
file_lines = file_content.splitlines()



# Position
job_title = 'Software Engineer'

for line in file_lines:
    if job_title in line:
        print(line)