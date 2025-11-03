# 1. Declare and assign the variables here:

shuttle_name = 'Determination'
shuttle_speed_mph = 17500
distance_to_mars_km = 225000000
distance_to_moon_km = 38400
MILES_PER_KM = 0.621

# 2. Use print() to print the 'type' each variable. Print one item per line.

print(type(shuttle_name))
print(type(shuttle_speed_mph))
print(type(distance_to_mars_km))
print(type(distance_to_moon_km))
print(type(MILES_PER_KM))


# Code your solution to exercises 3 and 4 here:
## Get the miles  to mars
miles_to_mars = distance_to_mars_km * MILES_PER_KM
print(f"miles to mars:{miles_to_mars}")

## How many days will it take to reach the mars
hours_to_mars = miles_to_mars/shuttle_speed_mph
print(f"hours to mars:{hours_to_mars}")
days_to_mars = hours_to_mars/24
print(f"days to mars:{days_to_mars}")

print(f"{shuttle_name} will take {days_to_mars} days to reach Mars.")


# Code your solution to exercise 5 here
#Get the miles to the moon:
miles_to_moon = distance_to_moon_km * MILES_PER_KM
print(f"miles to moon: {miles_to_moon}")
## How many days will it take to reach the moon:
hours_to_moon = miles_to_moon/shuttle_speed_mph
print(f"hours to moon:{hours_to_moon}")
days_to_moon = hours_to_moon/24
print(f"days to moon:{days_to_moon}")

print(f"{shuttle_name} will take {days_to_moon} days to reach Moon.")



