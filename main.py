# Import required modules
import random
import os
import sys
import json
from getkey import getkey, keys

if os.name == "nt":
    clear = "cls"
else:
    clear = "clear"

db = json.load(open("save.json"))
cheatcode = False

# This is sort of a joke
class Alarm(Exception):
    pass
    
try:
    argv = sys.argv[1]
    # print(argv)
    if argv == "dev":
        print("[⚠️ ⚠️ ⚠️ ]: Dev mode. Certain things may break.")
        cheatcode = True
        print("[NOTE]: Cheat code registered.")
        input("Press enter to continue...")
    elif argv == "reset-data":
        db["first_time"] = True
        db["stage"] = 1
        with open('save.json', 'w') as f:
            json.dump(db, f)
        print("[NOTE]: Your data has been reset.")
        exit()
    elif argv == "debug":
        print("Yep, all good. You would get errors if this didn't come up")
        exit()
    else:
        print("[ERROR]: Why did you try?")
        raise Alarm("⚠️CHEATER!⚠️")
except KeyError:
    print("This program comes with a file with '.json' at the end. If you're receiving this error, that file may be corrupted or does not exist. Can you please check that?")
    exit()
except IndexError:
    print("[NOTE]: Cheat code bypassed.")

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

        print(f"Press '{self.current_key}' to climb!")
        key = getkey()
        if key == self.current_key:
            self.position += 1
            if self.position > self.max_height:
                self.position = self.max_height
            os.system(clear)
            if self.position == 1:
                print(f"Climbed 1 up. You are now at {self.position} meter.")
            else:
                print(f"Climbed 1 up. You are now at {self.position} meters.")
        elif key == keys.ESC:
            return False
        else:
            fall_distance = 1
            if self.position > 5:
                os.system(clear)
                print(f"Fell from height {self.position}. You died!")
                self.alive = False
                return False
            else:
                self.position = max(0, self.position - fall_distance)
                os.system(clear)
                print(f"Waited and fell to position: {self.position}")

        self.current_key = random.choice(self.keys)
        return True

def climb():
    # Usage example
    climber = ClimbingSystem()
    print("Start climbing! Press what key is present when prompted.")
    print("You need to climb up to 10 meters.")
    print("Press any other key to wait (and fall).")
    print("Press 'ESC' to stop climbing.")
    print("If you fall from a height greater than 5 meters, you die!")

    while climber.position < climber.max_height and climber.alive:
        if not climber.climb():
            break

    if climber.position >= climber.max_height:
        print("Congratulations! You reached the top!")
        return True
    elif not climber.alive:
        print("Game Over. You died from falling.")
        return False
    else:
        print("You stopped halfway and fell, dying in the process.")
        return False


os.system(clear)
print("[NOTE]: Successfully launched game.")

# CODE STARTS HERE
print("WELCOME!")
start = input("Do. \nYou. \nWish. \nTo. \nPlay. \nMy. \nGame? \n").upper()

if start == "YES":
    pass
else:
    print("You really don't want to play it, don't you?")
    with open('save.json', 'w') as f:
        json.dump(db, f)
    exit()
os.system(clear)


def sequence1():
    print("Good. Let's begin.")
    print("""
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
        print("Correct. You have survived.")
        print(
            "The door of the locked payphone opens, and you see a cliff before your eyes."
        )
    elif no == 000:
        print("You really think the police can help you? I don't think so.")
        print("The payphone shocks you hard, killing you in the process. ")
        print("You. Are. Dead.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    elif cheatcode:
        pass
    else:
        print("Wrong number.")
        print("The payphone shocks you hard, killing you in the process. ")
        print("You. Are. Dead.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    db['stage'] = 2
    with open('save.json', 'w') as f:
        json.dump(db, f)


def sequence2():
    print(
        "You are now surrounded by walls, you don't know how they got there, but you cannot climb them. They are covered in oil. There is, however, a cliff in front of you."
    )
    print("You decide to climb.")
    input("Press enter to continue...")
    os.system('clear')
    climb_result = climb()  # Climbing system initation
    if climb_result:
        pass
    elif not climb_result:
        print("You. Are. Dead.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    print("You have reached the top of the cliff.")
    os.system('clear')
    with open('save.json', 'w') as f:
        json.dump(db, f)
    db['stage'] = 3


def sequence3():
    print(
        "You reach a treasure area with a pot of gold, but the same phone booth is there."
    )
    print("You are scared that the phone booth will attack you.")
    choice = input("Do you wish to take the gold? Or do you run away? (get gold/run away)").upper()
    if choice == "GET GOLD":
        print(
            "Lucky for you, the phone booth was a prop and did not do anything. You were able to retrieve the gold and win!"
        )

        print("You. Won.")
        x = input("Do you wish to save your data [yes/no]? ").upper()
        if x == "YES":
            db['stage'] = 4
            print("Your data is kept. You can now exit the game.")
            with open('save.json', 'w') as f:
                json.dump(db, f)
        else:
            db['stage'] = 1
            print("Your data has been wiped. Thank you for playing!")
            with open('save.json', 'w') as f:
                json.dump(db, f)
        exit()
    elif choice == "RUN AWAY":
        print(
            "Had you have known that the phone booth was a prop, you could have actually got the gold."
        )
        print(
            "Oblivious to the environment around you, you fall off the cliff")
        print("You. Are. Dead.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    else:
        print(
            "That's not an option, but the computer recognises that and bans you for cheating. What an idiot you are :/"
        )
        return False


while db['stage'] != 4:
    try:
        if db['stage'] == 1:
            sequence1()
        elif db['stage'] == 2:
            sequence2()
        elif db['stage'] == 3:
            a = sequence3()
            if not a:
                print(
                    "You are now banned. Because of how good you are, all of your progress has reset. You will have to restart the game."
                )
                db['stage'] == 1
                with open('save.json', 'w') as f:
                    json.dump(db, f)
                exit()
        elif db['stage'] == 4:
            break
        else:
            raise Alarm('What the heck happened here?')
    except KeyError:
        sequence1()
if db['stage'] == 4:
    print("You've won the game already.")
    x = input("Do you wish to keep your data [yes/no]? ").upper()
    if x == "YES":
        print("Alright then.")
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()
    else:
        db['stage'] = 1
        print(
            "Game successfully reset. You will now start from the beginning next time you load."
        )
        with open('save.json', 'w') as f:
            json.dump(db, f)
        exit()



        
