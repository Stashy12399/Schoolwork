import math

# needed module for rounding the km to 1 decimal place

miles_to_singapore = int(7017.2)
flight_cost = int(900)
# needed variables
print("Flight Problem by Stan- 24/09/21")
# just the title
print("Distance from PLC to Singapore City is : ", miles_to_singapore, "Miles")
km_to_singapore = miles_to_singapore * 1.60935
# formula to convert miles to km
km_to_singapore_rounded = round(km_to_singapore, 1)
# rounds the km unit to 1 decimal place
print("This means that there are ", km_to_singapore_rounded, "kilometers to Singapore")
cost_of_flight = km_to_singapore_rounded * 900
print(
    "Therefore, a flight to Singapore, that will charge €900 per km, will cost:",
    f"{cost_of_flight:,}",
    "€",
)
# the -  f"{cost_of_flight:,} - part in the string causes the cost of flight to be separated by a comma, making it easier for the user to read it

# ok so this was also homework , we had to get the distance from my school to singapore in miles, then convert that distance to km , and then calculate the cost of a 
# helicopter flight costing 900 euros per km, pretty basic , only noteworthy thing was the f"{cost_of_flight:,}" part, :D
