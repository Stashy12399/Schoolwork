# my first full project in python - its very basic and i made it in less than an hour
print("Unit Converter by Stan (its rather basic)")
#just the title of the project i guess
def unit_converterthebest():   
    number_2 = 1000
    choice = int(input("Type 1 for litre to ml , Type 2 for ml to litre : "))
    if choice >= 3:
        print("Please enter either 1 or 2")
        unit_converterthebest()
    
    if choice == 1:
        print("You have chosen the Litre to Mililitre converter")
        number_1 = int(input("Enter a litre that you want to convert to ml: "))
        result= number_1*number_2
        print(result)
        
    elif choice == 2:
        print("You have chosen the Mililitre to Litre Converter")
        number_12 = int(input("Enter a mililitre that you want to convert to litre: "))
        result2= number_12/number_2
        print(result2)
#entire function of the unit converter, you can change the units if you want to change it to kg to g etc
try:
    unit_converterthebest()
except ValueError  as e:
    print("you entered a letter , not a number")
#error catcher :) (im a fkn god)
 
# this was my first proper project , super basic since its only multiplying stuff but oh well here it is





