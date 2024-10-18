total_tasks = 20
tasks_ok = int(input('Enter the amount of solved tasks: '))
percentage = tasks_ok / total_tasks
if percentage >= 0.5 :
    print(f'You have passed the test! The percentage of correct tasks is {percentage * 100}%')
else:
        print(f'You have failed the test. The percentage of correct tasks is {percentage * 100}%')
