# Import required modules
import random
import os
import sys
import json
from getkey import getkey, keys
from rich.console import Console

console = Console()
try:
    db = json.load(open("save.json", "r"))
except FileNotFoundError:
    console.print("The save.json file was not found, or it was corrupted. Please retrieve it and put it in this working directory.")
    exit(1)
cheatcode = False

class Alarm(Exception):
    pass
    
try:
    argv = sys.argv[1]
    console.print(argv)
    if argv == "dev":
        console.print("[⚠️ ⚠️ ⚠️ ]: Dev mode. Certain things may break.")
        cheatcode = True
        console.print("[NOTE]: Cheat code registered.")
        input("Press enter to continue...")
    elif argv == "reset-data":
        db["first_time"] = True
        db["stage"] = 1
        with open('save.json', 'w') as f:
            json.dump(db, f)
        console.print("[NOTE]: Your data has been reset.")
        exit()
    elif argv == "debug":
        console.print("Yep, all good. You would get errors if this didn't come up")
        exit()
    else:
        console.print("[ERROR]: Why did you try?")
        
except KeyError:
    console.print("This program comes with a file with '.json' at the end. If you're receiving this error, that file may be corrupted or does not exist. Can you please check that?")
    exit()
except IndexError:
    console.print("[NOTE]: Cheat code bypassed.")

if not db["first_time"]:
    pass
else:
    db["first_time"] = True


if db['first_time']:
    db["first_time"] = False
    db['stage'] = 1


# Class for climbing system
class ClimbingSystem:
    def __init__(self):
        self.position = 0
        self.max_height = 10
        self.keys = [
            'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd',
            'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm'
        ]
        self.current_key = random.choice(self.keys)
        self.alive = True

    def climb(self):
        if not self.alive:
            return False

        console.print(f"Press '{self.current_key}' to climb!")
        key = getkey()
        if key == self.current_key:
            self.position += 1
            if self.position > self.max_height:
                self.position = self.max_height
            console.clear()
            console.clear()
            if self.position == 1:
                console.print(f"Climbed 1 up. You are now at {self.position} metre.")
            else:
                console.print(f"Climbed 1 up. You are now at {self.position} metres.")
        elif key == keys.ESC:
            return False
        else:
            fall_distance = 1
            if self.position > 5:
                console.clear()
                console.clear()
                console.print(f"Fell from height {self.position}. You died!")
                self.alive = False
                return False
            else:
                self.position = max(0, self.position - fall_distance)
                console.clear()
                console.clear()
                console.print(f"Waited and fell to position: {self.position}")

        self.current_key = random.choice(self.keys)
        return True

def climb():
    # Usage example
    climber = ClimbingSystem()
    console.print("To start climbing, press the key that is shown.")
    console.print("You need to climb up to 10 metres to succeed.")
    console.print("Pressing any other key or waiting will make you fall.")
    console.print("Press 'ESC' to stop climbing.")
    console.print("If you fall from a height greater than 5 metres, you die!")

    while climber.position < climber.max_height and climber.alive:
        if not climber.climb():
            break

    if climber.position >= climber.max_height:
        console.print("Congratulations! You reached the top!")
        return True
    else:
        console.print("Game Over. You died from falling.")
        return False


console.clear()
console.clear()
console.print("[NOTE]: Successfully launched game.")

# CODE STARTS HERE
console.print("WELCOME!")
start = input("Do. \nYou. \nWish. \nTo. \nPlay. \nMy. \nGame? \n[y/n] ").upper()
if "Y" in start:
    pass
else:
    console.print("You really don't want to play it, don't you?")
    with open('save.json', 'w') as f:
        json.dump(db, f)
    exit()
console.clear()
console.clear()


def sequence1():
    console.print("Good. Let's begin.")
    console.print("""
You are at a payphone, and you have a piece of paper reading:
Some of us contain 10 numbers, some of them don't.
The three-digit ones, will not help you at all.
Any number starting or ending with 13 does not help you.
The number is 12094444--
But what's the last two numbers?
It's between 10 and 20, but it's prime only.
And here's the answer: The last digit is a multiple of 3""")
    no = int(input("What's the number? "))
    if no == 1209444419:
        console.print("Correct. You have survived.")
        console.print(
            "The door of the locked payphone opens, and you see a cliff before your eyes."
        )
    elif no == 000:
        console.print("You really think the police can help you? I don't think so.")
        console.print("The payphone shocks you hard, killing you in the process. ")
        console.print("You. Are. Dead.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    elif cheatcode:
        pass
    else:
        console.print("Wrong number.")
        console.print("The payphone shocks you hard, killing you in the process. ")
        console.print("You. Are. Dead.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    db['stage'] = 2
    with open('save.json', 'w') as f:
        json.dump(db, f)


def sequence2():
    console.print(
        "You are now surrounded by walls, you don't know how they got there, but you cannot climb them. They are covered in oil. There is, however, a cliff in front of you."
    )
    console.print("You decide to climb.")
    input("Press enter to continue...")
    console.clear()
    console.clear()
    climb_result = climb()  # Climbing system initation
    if climb_result:
        pass
    elif not climb_result:
        console.print("You. Are. Dead.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    console.print("You have reached the top of the cliff.")
    console.clear()
    console.clear()
    with open('save.json', 'w') as f:
        json.dump(db, f)
    db['stage'] = 3


def sequence3():
    console.print(
        "You reach a treasure area with a pot of gold, but the same phone booth is there."
    )
    console.print("You are scared that the phone booth will attack you.")
    choice = input("Do you wish to take the gold? Or do you run away? (get gold/run away) ").upper()
    if choice == "GET GOLD":
        console.print(
            "Lucky for you, the phone booth was a prop and did not do anything. You were able to retrieve the gold and win!"
        )

        console.print("You. Won.")
        x = input("Do you wish to save your data [yes/no]? ").upper()
        if x == "YES":
            db['stage'] = 4
            console.print("Your data is kept. You can now exit the game.")
            with open('save.json', 'w') as f:
                json.dump(db, f)
        else:
            db['stage'] = 1
            console.print("Your data has been wiped. Thank you for playing!")
            with open('save.json', 'w') as f:
                json.dump(db, f)
        exit()
    elif choice == "RUN AWAY":
        console.print(
            "Had you have known that the phone booth was a prop, you could have actually got the gold."
        )
        console.print(
            "Oblivious to the environment around you, you fall off the cliff")
        console.print("You. Are. Dead.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    else:
        console.print(
            "That's not an option, but the computer recognises that and bans you for cheating. What an idiot you are :/"
        )
        return False


while db['stage'] != 4:
    try:
        stage = db['stage']
        if True:
            if stage == 1:
                sequence1()
            elif stage == 2:
                sequence2()
            elif stage == 3:
                a = sequence3()
                if not a:
                    console.print(
                        "You are now banned. Because of how good you are, all of your progress has reset. You will have to restart the game."
                    )
                    db['stage'] == 1
                    with open('save.json', 'w') as f:
                        json.dump(db, f)
                    exit()
            elif stage == 4:
                break
            else:
                raise Alarm('What the heck happened here?')
    except KeyError:
        sequence1()
if db['stage'] == 4:
    console.print("You've won the game already.")
    x = input("Do you wish to keep your data [yes/no]? ").upper()
    if x == "YES":
        console.print("Alright then.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    else:
        db['stage'] = 1
        console.print(
            "Game successfully reset. You will now start from the beginning next time you load."
        )
        with open('save.json', 'w') as f:
            json.dump(db, f)
        



        
