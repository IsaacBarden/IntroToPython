#Dice roller, as (a kind of bad) object usage example
import random


class Dice:
    def __init__(self, number, sides):
        self.number = number
        self.sides = sides
    def roll(self):
        total = 0
        for i in range(self.number):
            i = i #Warning suppression
            roll_result = random.randint(1, self.sides)
            print(roll_result, end=" ")
            total += roll_result
        print()
        print(f"Total: {total}")


roll_text = input("Roll some dice (format-#d#): ")
if (len(roll_text) > 3):
    try:
        dice_info = roll_text.split("d")
        if(len(dice_info) == 2):
            dice_number = int(dice_info[0])
            dice_sides = int(dice_info[1])
            my_dice = Dice(dice_number, dice_sides)
            my_dice.roll()
        else:
            print("Invalid roll")
    except:
        print("Invalid roll")
else:
    print("Invalid roll")