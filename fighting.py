# Bron - Team 19
# Fighting Engine
# Player vs Computer
# Exchange attacks until a player is dead

import random


def main():
    """Main function that will welcome the player to the game."""


    print("Welcome to the game!")
    print("")
    print("How to Play")
    print("")
    print("Fight against the computer in an battle using a range of atacks")
    print("Different types of attack will do various ammounts of damage")
    print("You can also choose to skip the attack and heal")
    print("Any move you make can miss, so choose wisely!")

    again = True

    # Set up the play again loop
    while again:
        winner = None
        playerhealth = 100
        enemyhealth = 100

        # determine whose turn it is
        turn = random.randint(1,2) # heads or tails
        if turn == 1:
            turn_player = True
            turn_enemy = False
            print("You will go first.")
        else:
            turn_player = False
            turn_enemy = True
            print("Your enemy will go first.")


        print("Your health: ", playerhealth, "Enemy health: ", enemyhealth)

        # set up the main game loop
        while (playerhealth != 0 or enemyhealth != 0):

            heal = False # determine if heal has been used by the player. Resets false each loop.
            miss = False # determine if the chosen move will miss.

            # create a dictionary of the possible moves and randomly select the damage it does when selected

            moves = {"Punch": random.randint(15, 25),
                     "Kick": random.randint(12, 35),
                     "Heal": random.randint(20, 30)}

            if turn_player:
                print("You can: ")
                print("1. Punch (15-25 Damage)")
                print("2. Kick (12-35)")
                print("3. Heal (Heal by 20-30)")
                playerchoice = input("Select a move: ").lower()
                chance_of_miss = random.randint(1,5) # 1 in 5 chance player misses

                if chance_of_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    playerchoice = 0 # player misses and deals no damage
                    print("You missed!")
                else:
                    if playerchoice in ("1", "punch"):
                        playerchoice = moves["Punch"]
                        print("\nYou used Punch. It dealt ", playerchoice, " damage.")
                    elif playerchoice in ("2", "kick"):
                        playerchoice = moves["Kick"]
                        print("\nYou used kick. It dealt ", playerchoice, " damage.")
                    elif playerchoice in ("3", "heal"):
                        heal = True # heal activated
                        playerchoice = moves["Heal"]
                        print("\nYou used Heal. It healed for ", playerchoice, " health.")
                    else:
                        print("\nThat is not a valid move. Please try again.")
                        continue

            else: # computer turn

                move_miss = random.randint(1,5)
                if move_miss == 1:
                    miss = True
                else:
                    miss = False

                if miss:
                    enemychoice = 0 # the computer misses and deals no damage
                    print("The computer missed!")
                else:
                    if enemyhealth > 30: 
                        if enemyhealth > 75:
                            enemychoice = moves["Punch"]
                            print("Your enemy used Punch. It dealt ", enemychoice, " damage.")
                        elif playerhealth > 35 and playerhealth <= 75: # computer decides whether to go big or play it safe
                            move_choice = ["Punch", "Kick"]
                            move_choice = random.choice(move_choice)
                            enemychhoice = moves[move_choice]
                            print("Your enemy used ", move_choice, ". It dealt ", enemychoice, " damage.")
                        elif playerhealth <= 35:
                            enemychoice = moves["Kick"] 
                            print("Your enemy used kick. It dealt ", enemychoice, " damage.")                       
                    else: # if the computer has less than 30 health, there is a 50% chance they will heal
                        choice5050 = random.randint(1,2) 
                        if choice5050 == 1:
                            heal = True
                            enemychoice = moves["Heal"]
                            print("Your enemy used Heal. It healed for ", enemychoice, " health.")
                        else:
                            if playerhealth > 75:
                                enemychoice = moves["Punch"]
                                print("Your enemy used Punch. It dealt ", enemychoice, " damage.")
                            elif playerhealth > 35 and playerhealth <= 75:
                                move_choice = ["Punch", "Kick"]
                                move_choice = random.choice(move_choice)
                                enemychoice = moves[move_choice]
                                print("Your enemy used ", move_choice, ". It dealt ", enemychoice, " damage.")
                            elif playerhealth <= 35:
                                enemychoice = moves["Kick"] 
                                print("Your enemy used kick. It dealt ", enemychoice, " damage.")

            if heal:
                if turn_player:
                    playerhealth += playerchoice
                    if playerhealth > 100:
                        playerhealth = 100 # cap max health at 100. No over healing!
                else:
                    enemyhealth += enemychoice
                    if enemyhealth > 100:
                        enemyhealth = 100
            else:
                if turn_player:
                    enemyhealth -= playerchoice
                    if enemyhealth < 0:
                        enemyhealth = 0 # cap minimum health at 0
                        winner = "Player"
                        break
                else:
                    playerhealth -= enemychoice
                    if playerhealth < 0:
                        playerhealth = 0
                        winner = "Enemy"
                        break
            print("Your health: ", playerhealth, "Enemy health: ", enemyhealth)

            # switch turns
            turn_player = not turn_player
            turn_enemy = not turn_enemy

        # once main game while loop breaks, determine winner and congratulate

        if winner == "Player":
            print("Player health: ", playerhealth, "Enemy health: ", enemyhealth)
            print("Congratulations! You won!!")
        else:
            print("Player health: ", playerhealth, "Enemy health: ", enemyhealth)
            print("Sorry, but you lost. Better luck next time.")

        print("\nWould you like to play again?")

        answer = input("> ").lower()
        if answer not in ("yes", "y"):
            again = False

main()
