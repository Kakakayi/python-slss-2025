# Choose Your Own Adventure
# Karina Luo
# 24 Sep 2025
import random
import time

# Choose your own adventure story focusing on
# Using variables and branching/conditionals
# Introduction
health = 3
gold = 0
user_name = input("Enter a user name.")
print("Starting amount of health: 3, starting amount of gold: 0")
while True:
    choice = int(
        input(
            f"Ok.{user_name} so here's three treasures. Which do you want to open? 1/2/3."
        )
    )
    treasures = ("gold + 1", "fight with boss", "nothing inside:(")
    r = [random.choice(treasures), random.choice(treasures), random.choice(treasures)]
    print(f"treasure1 = {r[0]}")
    print(f"treasure2 = {r[1]}")
    print(f"treasure3 = {r[2]}")
    w = choice - 1
    print(f"You've chosen {r[w]}!!!")
    time.sleep(0.5)
    if r[w] == "gold + 1":
        gold += 1
        print("Horray!!")
        print(f"current gold: {gold}")
    elif r[w] == "fight with boss":
        print("I'm sorry, you have to fight with the boss.")
        time.sleep(0.5)
        boss_health = 10
        player_health = 10
        print("You are in the battle field now.")
        time.sleep(1)
        print("\nYou and the boss both have 10 points of health. ")
        time.sleep(1)
        print("\nYou will take turns attacking or defending ")
        time.sleep(1)
        print("\nDefending means reducing half of the boss' next attack")
        time.sleep(1)
        print("\nThe game ends when one side has no more health.")
        while True:
            boss_damage = random.randint(1, 5)
            player_damage = random.randint(1, 5)
            player_choice = input("\nDo you want to attack or defend?")
            choice = ("attack", "defend")
            x = random.choice(choice)
            if player_choice.lower() == "attack" and x == "attack":
                print("Ok, you and the boss both chose to attack. \nBattle begins")
                boss_health -= player_damage
                player_health -= boss_damage
                print(f"""current statistic:
                    player health = {player_health}
                    boss health = {boss_health}
                    player damage = {player_damage}
                    boss damage = {boss_damage}""")
                time.sleep(1)
            elif player_choice.lower() == "attack" and x == "defend":
                print("Ok, you chose to attack, and the boss chose to defend.")
                boss_health -= player_damage / 2
                print(f"""current statistic:
                    player health = {player_health}
                    boss health = {boss_health}
                    player damage(originally) = {player_damage}
                    player damage after defending = {player_damage / 2}
                    boss damage = n/a """)
                time.sleep(1)
            elif player_choice.lower() == "defend" and x == "attack":
                print("Ok, boss chooses to attack, and you choose to defend.")
                player_health -= boss_damage / 2
                print(f"""current statistic:
                    player health = {player_health}
                    boss health = {boss_health}
                    boss damage(originally) = {boss_damage}
                    boss damage after defending = {boss_damage / 2}
                    player damage = n/a """)
                time.sleep(1)
            else:
                print("Both chooses to defend--> nothing happens")
            if boss_health <= 0 and player_health > 0:
                print("Horray!!! You win")
                gold += 20
                print("You win 20 gold!")
                print(f"current amount of gold: {gold}")
                break
            elif boss_health > 0 and player_health <= 0:
                print("I'm sorry. You lost the game.")
                print("Health -1")
                health -= 1
                print(f"current health: {health}")
                break
            elif boss_health == 0 and player_health == 0:
                print("Tie!!! Nothing happens.")
    else:
        print("umm, not too bad.")
    if health == 0:
        print("uh oh. you die. forced to quit\n sorry.")
        break
    exit = input("type 'quit' to stop and exit and 'continue' to continue")
    if exit.lower().strip("!. ,") == "quit":
        print("kk, bye~ have a good day!:stuck_out_tongue:")
        break
    else:
        pass
