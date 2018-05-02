name = 'Faiz Mokhtar'
age = 25
height = 100
weight = 60
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height}cm tall.")
print(f"He's {weight}kg heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

height_in_inches = height / 2.54
weight_in_pound = weight / 0.45359237

print(f"His height in inches is {height_in_inches:.2f}\"")
print(f"His weight in pound is {weight_in_pound:.2f}\"")
