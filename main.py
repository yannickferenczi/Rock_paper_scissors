import os, sys
from random import choice
from time import sleep

CHOICES_LIST = ["pierre", "papier", "ciseaux"]

def typing_print(text):
    """Display the text with a typing effect."""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.05)

def typing_input(text):
    """Display the text of an input with a typing effect."""
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        sleep(0.05)
    value = input()
    return value

def choice_is_valid(player_choice):
    """Return True is player_choice in CHOICES_LIST"""
    return player_choice in CHOICES_LIST

def play_again():
    """Start a new game or shut down the program"""
    print()
    try_again = typing_input("Nouvelle partie? (y/n) ")
    print()
    if try_again == "y":
        pass
    elif try_again == "n":
        sys.exit(0)
    else:
        typing_print("Ta décision n'est pas claire!")
        return play_again()


def computer_plays():
    """Defines the hand of the computer"""
    return choice(CHOICES_LIST)

def player_plays():
    """
    Ask the player to choose between rock, paper, and cisors.
    
    The function keeps asking the player until it gets a valid answer.
    """
    print()
    player_choice = typing_input("Choisi ton arme: " )
    if choice_is_valid(player_choice):
        return player_choice
    else:
        typing_print(
"""
Ton choix n'est pas valide! Merci de choisir parmi les
options suivantes (la casse est prise en compte):

pierre
papier
ciseaux

"""
        )
        return player_plays()

def there_is_a_winner(computer_move, player_move):
    return computer_move != player_move

def player_wins(computer_move, player_move):
    if (
        (player_move == "papier" and computer_move == "pierre")
        or
        (player_move == "ciseaux" and computer_move == "papier")
        or
        (player_move == "pierre" and computer_move == "ciseaux")
    ):
        return True


if __name__ == "__main__":
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")
    typing_print(
"""
Salut jeune aventurier, et bienvenue pour une partie de pierre,
papier ou ciseaux!

Pour jouer, c'est simple: tape ton choix en toutes lettres et tout
en minuscule. Les seules entrées acceptées sont 'pierre' 'papier'
ou 'ciseaux'.

"""
    )

    computer_points = 0
    player_points = 0

    while True:
        computer_move = computer_plays()
        player_move = player_plays()
        print()
        if there_is_a_winner(computer_move, player_move):
            if player_wins(computer_move, player_move):
                player_points += 1
                typing_print(
"Félicitations, tu as vaincu l'ordinateur! " +
f"Il avait choisi '{computer_move}'."
                )
            else:
                computer_points += 1
                typing_print(
"Dommage, l'ordinateur a eu plus de chance. " +
f"Il avait choisi '{computer_move}'."
                )
        else:
            typing_print("Egalité! Recommencez...")
            print()
            continue

        typing_print(
f"""
Tu as {player_points} point{'s' if player_points > 1 else ""}.
L'ordinateur a {computer_points} point{'s' if computer_points > 1 else ""}.
"""
        )

        play_again()
