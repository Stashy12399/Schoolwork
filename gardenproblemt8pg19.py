print("Garden Calculator made by Stan - 14/9/21")
l = float(input("enter the length of the garden (meters)"))
w = float(input("enter the width of the garden in meters"))
l_2 = float(input("enter the length of the house in  the garden in meters"))
w_2 = float(input("enter the width of the house in the garden in meters"))
# all the inputs for the areas
garden_area = l * w
garden_areastr = str(garden_area)
# multiplying garden length by the width to find area and then converting it to a string
house_area = l_2 * w_2
house_areastr = str(house_area)
# multiplying house length by the width of the house and then converting it to a string
gardenareap = garden_area - house_area
gardenareapstr = str(gardenareap)
# garden area minus the house area and converting the result to a string
print("the area of the garden, excluding the house is: " + gardenareapstr + " meters squared")
time = gardenareap / 2
# divides the garden area by 2 to get the time you need to cut all the grass
timeinseconds = round(time, 2)
# rounds the time to 2 decimal places
timestr = str(timeinseconds)
# convert to string
minutes = timeinseconds / 60
# converting the seconds to minutes
roundedmins = round(minutes, 2)
# rounding the mins to 2 decimals
minutesstr = str(roundedmins)
print("It will take " + minutesstr + " minutes to cut all the grass!!, (which is " + timestr + " seconds)")
# result!!!

# this was homework , so basically we gotta get the user input on area of a garden, then an area of a house in the garden then calculate the time it takes to cut
# all the grass in the garden at a fixed rate
