food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
food_list = food.split(",")
print(food_list)
equipment_list = equipment.split(",")
print(equipment_list)
pets_list = pets.split(",")
print(pets_list)
sleep_aids_list = sleep_aids.split(",")
print(sleep_aids_list)


# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.

cargo_hold = [food_list, equipment_list, pets_list, sleep_aids_list]
print("Cargo Hold:", cargo_hold)

# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.

print("\nCargo Hold Cabinets:")
print("0 - Food")
print("1 - Equipment")
print("2 - Pets")
print("3 - Sleep Aids")

user_choice = int(input("\nSelect a cabinet number (0 - 3): "))

# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.

if 0 <= user_choice <= 3:
    print("\nYou selected cabinet {}.".format(user_choice))
    print("Contents: {}".format(cargo_hold[user_choice]))
else:
    print("\nError: Invalid cabinet number! Please choose between 0 and 3.")

# e) Modify the code to query the user for BOTH a cabinet in cargo_hold AND a particular item. 
# Use the in method to check if the cabinet contains the selected item, then print “Cabinet ____ DOES/DOES NOT contain ____.”
cabinet = int(input("Select a cabinet (0 - 3): "))

if 0 <= cabinet <= 3:
    print(f"Cabinet {cabinet} contains: {cargo_hold[cabinet]}")
    
    # Ask for an item to check
    item = input("Enter an item to check: ")
    
    if item in cargo_hold[cabinet]:
        print(f"Cabinet {cabinet} DOES contain {item}.")
    else:
        print(f"Cabinet {cabinet} DOES NOT contain {item}.")
else:
    print("Invalid cabinet number! Please choose between 0 and 3.")
