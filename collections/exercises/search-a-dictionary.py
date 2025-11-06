flavors = {
  'chocolate' : 0.35,
  'vanilla' : 0.35,
  'strawberry' : 0.42,
  'cookies and cream' : 0.45,
  'mint chocolate chip' : 0.42,
  'fudge chunk' : 0.45,
  'saffron' : 2.25,
  'garlic' : 0.05
}

## Set a variable called choice to the flavor you want to search for.

choice = 'saffron'  
## Use an if statement to check if choice is in the flavors dictionary.
if choice in flavors:
    print(choice, flavors[choice])

## If it is, set another variable called cost to the value associated with choice.
## If it isn’t, set cost to 0.
if choice in flavors:
    cost = flavors[choice]   
else:
    cost = 0  
## Print the cost.
print("Cost:", cost)
### Search a Dictionary Part 2:

## Initialize two variables: highest_cost to 0 and fanciest to an empty string.
highest_cost = 0
fanciest = {}

## Loop through the flavors dictionary using a for loop.
for key in flavors.keys():
    print(key, flavors[key])

## For each flavor, check if its price is higher than highest_cost.
## If it is, update fanciest to this flavor and highest_cost to its price.
for flavor in flavors:                     # loop through each flavor
    if flavors[flavor] > highest_cost:     # compare price
        print("The {} flavor costs ${:.2f}, which is greater than the highest_cost.".format(flavor, flavors[flavor]))
## If it is, update fanciest to this flavor and highest_cost to its price.
## After the loop, print the most expensive flavor.
    
for flavor in flavors:
    if flavors[flavor] > highest_cost:
        highest_cost = flavors[flavor]   # update highest price
        fanciest = flavor                # update flavor name
        print(flavor, "is now the highest at $", highest_cost)

print("\nThe fanciest flavor is:", fanciest)
print("It costs $", highest_cost)
