# Input: slices each person eats
person_1 = int(input("Enter how many slices person 1 eats: "))
person_2 = int(input("Enter how many slices person 2 eats: "))
person_3 = int(input("Enter how many slices person 3 eats: "))
person_4 = int(input("Enter how many slices person 4 eats: "))

# Processing: total slices required
total_slices = person_1 + person_2 + person_3 + person_4
pizzas_required = total_slices // 8
leftover_slices = total_slices % 8

# Output: total pizzas and leftover slices
print(f"Pizzas required: {pizzas_required}")
print(f"Leftover slices: {leftover_slices}")
