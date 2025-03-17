import random
import time


def print_pause(message, wait_time=1):
    print(message)
    time.sleep(wait_time)


def intro():
    print_pause(
        "You find yourself standing in an open field, surrounded by "
        "tall grass and yellow wildflowers.")
    print_pause(
        "Rumor has it that a dangerous creature "
        "is lurking nearby, terrorizing the village.")
    print_pause("In front of you stands a mysterious house.")
    print_pause("To your right, you see a dark cave.")
    print_pause("To your left, there's an old armory.")
    print_pause(f"In your hand, you hold your trusty (but weak) {weapon}.")


def field():
    print_pause("\nEnter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("Enter 3 to explore the armory.")
    print_pause("What would you like to do?")
    choice = input("Please enter 1, 2, or 3: ")
    if choice == '1':
        house()
    elif choice == '2':
        cave()
    elif choice == '3':
        armory()
    else:
        print_pause("Invalid choice, try again.")
        field()


def cave():
    global cave_visited, weapon
    print_pause("You carefully step into the dark cave.")
    if cave_visited:
        print_pause("You've been here before. The cave is now empty.")
    else:
        print_pause("Your eyes catch a glint of metal behind a rock!")
        print_pause("You have found the powerful Sword of Ogoroth!")
        print_pause(f"You discard your {weapon} and take the sword.")
        weapon = "Sword of Ogoroth"
        cave_visited = True
    print_pause("You return to the field.")
    field()


def armory():
    global armory_visited, weapon
    print_pause("You step into the old armory, filled with ancient weapons.")
    if armory_visited:
        print_pause("There's nothing left to take.")
    else:
        print_pause("You find a mighty Battle Axe and a Bow & Arrow!")
        while True:
            weapon_choice = input(
                "Which one would you like? (Axe/Bow): ").strip().lower()
            if weapon_choice == "axe":
                weapon = "Battle Axe"
                break
            elif weapon_choice == "bow":
                weapon = "Bow & Arrow"
                break
            else:
                print_pause("Invalid choice, you leave empty-handed.")
            armory_visited = True
    print_pause("You return to the field.")
    field()


def house():
    print_pause("You cautiously approach the house.")
    print_pause(f"As you knock on the door, a {enemy} bursts out!")
    print_pause("It growls menacingly!")
    fight()


def fight():
    global lifes
    global game_running
    print_pause(f"The {enemy} lunges at you!")
    while True:
        action = input(
            "Do you want to fight or run? (fight/run): ").strip().lower()
        if action == "run":
            print_pause("You manage to escape back to the field!")
            field()
            return
        elif action == "fight":
            break
        else:
            print_pause("Invalid choice, try again.")

    if weapon in ["dagger"]:
        print_pause("Your weapon is too weak!")
        print_pause("The monster strikes you and you lose 1/3 of your life")
        lifes -= 1
        if lifes > 0:
            print_pause(f"You barely escape with your life remaining {lifes}!")
            print_pause("You run back to the field.")
            field()
        else:
            print_pause("You are dead")
            game_running = play_again()
    else:
        print_pause(f"You raise your {weapon} and prepare for battle!")
        if weapon == "Sword of Ogoroth":
            print_pause("With a swift strike, you slay the creature!")
        elif weapon == "Battle Axe":
            print_pause("You deliver a crushing blow, defeating the beast!")
        elif weapon == "Bow & Arrow":
            print_pause(
                "From a distance, you fire an arrow, striking the enemy down!")
        print_pause("The village is safe! You are victorious!")
        game_running = play_again()


def play_again():
      while True:
        choice = input("Would you like to play again? (y/n): ").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print_pause("Invalid choice, try again.")


def start_game():
    global weapon, cave_visited, armory_visited, enemy, game_running, lifes
    game_running = True
    while game_running:
        lifes = 3
        weapon = "dagger"
        cave_visited = False
        armory_visited = False
        enemies = ['troll', 'wicked fairie', 'pirate', 'gorgon', 'dragon']
        enemy = random.choice(enemies)
        intro()
        field()


# Start the game loop
game_running = True
start_game()
