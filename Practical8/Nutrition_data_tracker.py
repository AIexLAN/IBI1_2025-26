# Define a class representing a food item with its nutritional values
class food_item:
    def __init__(self, name, calories, protein, carbs, fat):
        self.name = name
        self.calories = calories
        self.protein = protein
        self.carbs = carbs
        self.fat = fat

# Create several food item instances
apple=food_item("apple",60,0.3,15,0.5)
burger=food_item("burger", 500, 25, 40, 30)
rice=food_item("rice", 200, 4, 45, 1)
cake=food_item('cake',500, 10, 40, 60)

# Function to compute total nutrition for a list of food items
def total_nutrition(food_list):
    total_calories = 0
    total_proteins=0
    total_carbonhydrate=0
    total_fat = 0
    # Iterate over each food object in the list
    # Add the nutritional values of the current food to the totals
    for food in food_list:
        total_calories+=food.calories
        total_proteins+=food.protein
        total_carbonhydrate+=food.carbs
        total_fat+=food.fat
    print("Total calories:", total_calories)
    print("Total protein:", total_proteins)
    print("Total carbs:", total_carbonhydrate)
    print("Total fat:", total_fat)

    # Issue a warning if total calories exceed 2500 or total fat exceeds 90g
    if total_calories>2500 or total_fat>90:
        print(f'WARNING!')

    return total_calories, total_proteins, total_carbonhydrate, total_fat

# Example usage:
my_food_today=[apple,burger,rice,cake]
total_nutrition(my_food_today)