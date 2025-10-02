print("=== PYTHON CONDITIONAL TESTS WITH PREDICTIONS ===\n")

# Test 1: Basic equality test
age = 25
print("Test 1: Basic Equality")
print(f"Testing: age = {age}, age == 25")
print("Prediction: This should be True because 25 equals 25")
if age == 25:
    print("Result: TRUE - Age is exactly 25")
else:
    print("Result: FALSE - Age is not 25")
print()

# Test 2: String comparison
name = "Alice"
print("Test 2: String Comparison")
print(f"Testing: name = '{name}', name == 'alice'")
print("Prediction: This should be False because Python is case-sensitive")
if name == "alice":
    print("Result: TRUE - Names match")
else:
    print("Result: FALSE - Names don't match (case matters)")
print()

# Test 3: Numeric range test
score = 85
print("Test 3: Range Testing")
print(f"Testing: score = {score}, 80 <= score < 90")
print("Prediction: This should be True because 85 is between 80 and 90")
if 80 <= score < 90:
    print("Result: TRUE - Score is in the B grade range")
else:
    print("Result: FALSE - Score is outside B grade range")
print()

# Test 4: List membership test
fruits = ['apple', 'banana', 'orange']
print("Test 4: List Membership")
print(f"Testing: fruits = {fruits}, 'grape' in fruits")
print("Prediction: This should be False because grape is not in the list")
if 'grape' in fruits:
    print("Result: TRUE - Grape is in the list")
else:
    print("Result: FALSE - Grape is not in the list")
print()

# Test 5: Boolean logic with AND
temperature = 22
humidity = 60
print("Test 5: Boolean AND Logic")
print(f"Testing: temperature = {temperature}, humidity = {humidity}")
print("Condition: temperature > 20 AND humidity < 70")
print("Prediction: This should be True because both conditions are met")
if temperature > 20 and humidity < 70:
    print("Result: TRUE - Weather is comfortable")
else:
    print("Result: FALSE - Weather is not comfortable")
print()

# Test 6: Boolean logic with OR
day = "Sunday"
is_holiday = False
print("Test 6: Boolean OR Logic")
print(f"Testing: day = '{day}', is_holiday = {is_holiday}")
print("Condition: day == 'Sunday' OR is_holiday == True")
print("Prediction: This should be True because it's Sunday, even though it's not a holiday")
if day == "Sunday" or is_holiday == True:
    print("Result: TRUE - It's a rest day")
else:
    print("Result: FALSE - It's a work day")
print()

# Test 7: NOT operator
is_raining = False
print("Test 7: NOT Operator")
print(f"Testing: is_raining = {is_raining}, not is_raining")
print("Prediction: This should be True because NOT False equals True")
if not is_raining:
    print("Result: TRUE - It's not raining, good for outdoor activities")
else:
    print("Result: FALSE - It's raining, stay indoors")
print()

# Test 8: Empty list/string test
shopping_list = []
print("Test 8: Empty Collection Test")
print(f"Testing: shopping_list = {shopping_list}, not shopping_list")
print("Prediction: This should be True because empty lists are falsy in Python")
if not shopping_list:
    print("Result: TRUE - Shopping list is empty")
else:
    print("Result: FALSE - Shopping list has items")
print()

# Test 9: Multiple conditions with elif
grade = 92
print("Test 9: Multiple Conditions (elif chain)")
print(f"Testing: grade = {grade} against multiple ranges")
print("Prediction: This should match the 'A' grade condition (90-100)")
if grade >= 90:
    print("Result: Grade A - Excellent!")
elif grade >= 80:
    print("Result: Grade B - Good!")
elif grade >= 70:
    print("Result: Grade C - Average")
else:
    print("Result: Grade F - Needs improvement")
print()

# Test 10: Type checking
value = "123"
print("Test 10: Type Checking")
print(f"Testing: value = '{value}', type(value) == str")
print("Prediction: This should be True because '123' is a string, not an integer")
if type(value) == str:
    print("Result: TRUE - Value is a string")
else:
    print("Result: FALSE - Value is not a string")
print()

print("=== ALL CONDITIONAL TESTS COMPLETED ===")





