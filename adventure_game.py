# You can use this workspace to write and submit your adventure game project.i
import time
import random
from datetime import datetime

weapons = ["Weaponized Social Media", "Drones with flying bombs"]
battlefields = ["Maripol", "Kiev"]
enemies = ["Russians", "Pro Russian Troops"]


weapon = random.choice(weapons)
battlefield = random.choice(battlefields)
enemy = random.choice(enemies)


def greeting():
    if datetime.today().hour > 18:
        return ("Dobryy vechir!")  # Good evening in Ukrainian
    else:
        return ("Dobroho ranku!")  # Good morning in Ukranian
    print(greeting())


def display(message):
    for n in range(len(message)):
        print(message[n])
        time.sleep(1)


def print_pause(message, pause=2):
    print(message)
    time.sleep(pause)


def intro():
    print_pause(f"{greeting()} Concerned citizens!")
    print_pause("You are now standing with all the Ukrainians...")
    print_pause(f"as you are under attack by the {enemy}!")
    print_pause(f"Equipped with the {weapon} from your global peace allies...")
    print_pause("Will you fight for the people of Ukraine, ")
    print_pause("or surrender to your enemy?")


def city(arsenal):
    if "Javelin Missiles" in arsenal:
        print_pause("you are now back in the alleys in the worn torn city... ")
        print_pause("Suddenly, you are surrounded by the evil invaders!")
        print_pause(f"the {enemy} are pressuring you to surrender ")
        print_pause("or die for the people")
    else:
        print_pause(f"You turned to the people in {battlefield}")
        print_pause("and the whole peace world supports you!")
        print_pause(f"the {enemy} are approaching with their tanks")
        print_pause(f"the kind people in {battlefield}...")
        print_pause("handed you the legendary Javelin Missiles")
        arsenal.append("Javelin Missiles")
    playeroption(arsenal)


def battle(arsenal):
    if "Javelin Missiles" in arsenal:
        print_pause(f"You aimed the Javelin Missiles and fired at the {enemy}")
        print_pause(f"The {enemy}'s tanks were blown to pieces in flames")
        print_pause("They surrendered!", 3)
        print_pause("You Win and the people of Ukraine Win!!!", 3)
    else:
        print_pause("You started the attack")
        print_pause(f"but the {enemy} blasted the whole alley around you!")
        print_pause("You lost consciousness...", 3)
        print_pause("The War is not over...but this game is.")
        print_pause("Please try again and support peace in Ukraine", 3)


def playeroption(arsenal):
    response = input(f"\n(1) Fight the {enemy} " "\n(2) Strategy retreat\n")
    if response == "1":
        battle(arsenal)
    elif response == "2":
        city(arsenal)
    else:
        print_pause("You have only two choices: pick 1 or 2 !")
        playeroption(arsenal)


def game_replay():
    print_pause("\n Would you like to start again?")
    replay = input("\n(1) Yes! Another Chance!\n(2) No, no more wars!\n")
    if replay == "1":
        print_pause("You choose Yes, let's give peace another chance!")
        print_pause("Start beaming you to Ukraine...")
        display("три два один")
        global weapon, battlefield, enemies
        weapon = random.choice(weapons)
        battlefield = random.choice(battlefields)
        enemy = random.choice(enemies)
        homelanddefender()
    elif replay != "2":
        print_pause("You have only two choices: pick 1 or 2 !\n")
        game_replay()
    else:
        print_pause("Do pobachennya i udachi", 3)  # Goodbye and good luck
        print_pause("Goodbye and good luck", 3)


def homelanddefender():
    arsenal = []
    intro()
    playeroption(arsenal)
    game_replay()

homelanddefender()

