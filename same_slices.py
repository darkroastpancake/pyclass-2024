# Input: slices per person
slices_per_person = int(input("How many slices does each person eat?: "))

# Processing: total slices required
total_slices = slices_per_person * 4
pizzas_required = total_slices // 8
leftover_slices = total_slices % 8

# Output: total pizzas and leftover slices
print(f"Pizzas required: {pizzas_required}")
print(f"Leftover slices: {leftover_slices}")