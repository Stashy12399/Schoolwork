import random
import math

# needed modules 

dim_selection = int(input("1 for choosing the dimensions of the cylinder \n2 for random dimensions"))


# allows the user to select whether they want to choose their own dimensions or just use a random value

def option1():
    cyl1_height = float(input("Enter the height of the cylinder in cm"))
    cyl1_radius = float(input("Enter the radius of the cylinder in cm"))
    cyl1_volume = cyl1_radius * cyl1_radius * 3.14 * cyl1_height
    cyl1_volumeint = int(cyl1_volume)
    totalliquid1 = random.randint(cyl1_volumeint, cyl1_volumeint + 1000)
    print("total volume of the cylinder = ", cyl1_volume)
    print("Total Liquid = ", totalliquid1)
    remainder1 = totalliquid1 / cyl1_volumeint
    if remainder1.is_integer():
        print(remainder1, " cylinders are needed to carry all the liquid")
    else:
        print(math.floor(remainder1 + 1), "cylinders are needed to carry all the liquid")


# function of all the calculations used if you select option one

def option2():
    cyl2_height = random.randint(1, 20)
    print("The height of the cylinder is :", cyl2_height, "cm")
    cyl2_radius = random.randint(1, 20)
    print("The radius of the cylinder is :", cyl2_radius, "cm")
    cyl2_volume = cyl2_radius * cyl2_radius * 3.14 * cyl2_height
    cyl2_volumeint = int(cyl2_volume)
    print("the volume of the cylinder is ", cyl2_volume, "cm3")
    totalliquid2 = random.randint(cyl2_volumeint, cyl2_volumeint + 1000)
    print("Total volume of liquid is ", totalliquid2, "cm3")
    remainder2 = totalliquid2 / cyl2_volumeint
    if remainder2.is_integer():
        print(remainder2, " cylinders are needed to carry all the liquid")
    else:
        print(math.floor(remainder2) + 1, "cylinders are needed to carry all the liquid")


# functions of all the calculations used if you select option two

if dim_selection == 1:
    option1()
elif dim_selection == 2:
    option2()
else:
    print("Please enter either 1 or 2 (rerun program)")
# calls the respective function if the user types in 1 or 2, and if they select something that isnt either of the 
# numbers it tells the user to choose 1 or 2 and to restart the program

# this is homework and as of 24/9/21 is my best project so far :D
