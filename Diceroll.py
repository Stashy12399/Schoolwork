import random
def randomint():
    a = int(input("Press 1 to roll the dice"))
    if a >= 1:
        print(random.randint(1,6))
        randomint()
randomint()
# just a diceroller based on the random number generator i previously made - its extremely basic( took me like 1 minute) , just accepts an input and spits out a random number between 1 and 6 and then repeats itself infinitely (no error catching so if you enter something that isnt a “1” the program breaks 
