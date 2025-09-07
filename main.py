# -------------------------------------------EL PYTHONCITO 🐍🐍🐍
from art import logo, vs
from game_data import data, emojis_correct
import random


def random_celebrity():
    """This function chooses an item from the list of celebrities."""
    return random.choice(data)


def compare_(first_c, second_c):
    print(f"➡️➡️️➡️➡️ Compare 🅰️: {first_c["name"]}, a {first_c["description"]}, from {first_c["country"]}.")
    print(vs)
    print(f"➡️➡️➡️➡️ Compare 🅱️: {second_c["name"]}, a {second_c["description"]}, from {second_c["country"]}.")


def higher_followers(first_c, second_c):
    """This function choose the higher celebrity."""
    first_counter = first_c["follower_count"]
    second_counter = second_c["follower_count"]

    if first_c["name"] != second_c["name"]:
        if first_counter > second_counter:
            correct_higher["a"] = first_c
            return first_c
        else:
            correct_higher["b"] = second_c
            return second_c
    else:
        correct_higher["a"] = first_c


def user_choose(user_A_B):
    """This function checks if the user's choice is correct."""
    for i in correct_higher:
        if i == user_A_B:
            return True
        else:
            return False


# -------------------------------------------------------------------------------------------------------
score = 0
user_failed = False

correct_higher = {}
first_celebrity = random_celebrity()
second_celebrity = random_celebrity()

while not user_failed:

    print(logo)
    if score > 0:
        print(f"CORRECT{random.choice(emojis_correct)}!!!! YOUR CURRENT SCORE: {score}")

    compare_(first_celebrity, second_celebrity)
    user_choose_A_or_B = input("\n🐍🐍🐍🐍 Who has more followers? Type '🅰️' or '🅱️': ").lower()
    higher_c = higher_followers(first_celebrity, second_celebrity)

    is_correct = user_choose(user_choose_A_or_B)
    if is_correct:
        first_celebrity = higher_c
        second_celebrity = random_celebrity()
        correct_higher = {}
        score += 1
    else:
        user_failed = True

    print("\n" * 500)

# -----------------------------------------------------------------------------------------------FINAL
print(f"Sorry that's wrong 😣!!! Final score {score}.")
input("\nType ENTER to finish!!!")
