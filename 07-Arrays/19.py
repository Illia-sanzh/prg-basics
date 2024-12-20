meal_plan = [
   ["Oatmeal", "Grilled Chicken Salad", "Spaghetti"],
   ["Pancakes", "Sandwich", "Steak"],
   ["Smoothie", "Chicken Wrap", "Salmon"],
   ["Eggs", "Pasta", "Soup"],
   ["Toast", "Burrito", "Pizza"],
   ["Cereal", "Salad", "Fish Tacos"],
   ["Bagel", "Rice and Beans", "Stir-fry"]
]

def weekday(n):
   weekdays = ["Monday", "Tuesday", "Wednesday",
      "Thursday", "Friday", "Saturday", "Sunday"]
   return weekdays[n-1]


def day_meal_plan(meal_plan, day_number):
    result = ''
    for i in range(len(meal_plan[0])):
        result += meal_plan[day_number - 1][i] + ', '
    return result

print(f'The meal plan for {weekday(1)} is {day_meal_plan(meal_plan, 1)}')