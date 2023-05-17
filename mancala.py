import os
import time
import random


#start message with option to see the rules
def start_message():
    print("Welcome to Mancala!")
    experience = input("Do you know how to play? (Y/N)\n").upper()
    if list(experience)[0]== "N":
        rules()
    elif list(experience)[0]== "Y":
        print("\nAwesome!")
        time.sleep(1)
    else:
        print("\nI'm not sure what that means...")
    print("\nIf you ever decide you need a refresher on the rules, just type 'rules'.")
    time.sleep(2)
    print("\nNow let's play!")
    time.sleep(1)
    display() 


#Game Rules Message
def rules():
    display()
    print("RULES:\n")
    print("The board consists of 12 pits, each with 4 seeds, and 2 empty bowls.\nYour pits are the 6 on the bottom and your bowl is above your name.")
    time.sleep(5)
    print("\nOn your turn you will pick one of your 6 pits.\nThe seeds will be redistributed, 1 per pit, counter-clockwise.\nIf you pass your bowl, a seed goes in there too.")
    time.sleep(5)
    print("\nIf your last seed lands in your bowl, you get a free turn!\nYou might be able to do this multiple times in a row if you plan well.")
    time.sleep(5)
    print("\nIf your last seed lands in one of your empty pits, you take the opposite pit’s seeds!\nThis only works if your opponent has seeds in the opposite pit.\nThose seeds are then auto-redistributed around the board like a regular turn.")
    time.sleep(5)
    print("\nThe game ends when one side does not have any seeds left in their 6 pits.\nThe final score counts both your bowl and any seeds you have left in your pits.\nBe careful not to run out of seeds in your pits if your opponent still has a lot in theirs!")
    time.sleep(6)
    print("\nThat's it, have fun!")

    input("\n[PRESS ANY KEY]")


#sets up visual board and clear/updates it after each move
def display():
    os.system('cls')
    title = "__Mancala__"
    gap = " "
    player_pit_lables = f"6{7*gap}5{7*gap}4{7*gap}3{7*gap}2{7*gap}1"
    comp_pit_lables = f"1{7*gap}2{7*gap}3{7*gap}4{7*gap}5{7*gap}6"
    comp_name = computer
    player_name = player
    vs = "--vs--"
    vs_space = 64 - len(comp_name) - len(player_name)
    header = f"{title:^64s}\n{comp_pit_lables:^64s}"
    comp_pits = f"{8*gap}({pits[8]:^5d}) ({pits[9]:^5d}) ({pits[10]:^5d}) ({pits[11]:^5d}) ({pits[12]:^5d}) ({pits[13]:^5d})"
    bowls = f"({pits[7]:^5d}){49*gap}({pits[0]:^5d})"
    player_pits = f"{8*gap}({pits[6]:^5d}) ({pits[5]:^5d}) ({pits[4]:^5d}) ({pits[3]:^5d}) ({pits[2]:^5d}) ({pits[1]:^5d})"
    footer = f"{player_pit_lables:^64s}\n{comp_name:<s}{vs:^{vs_space}s}{player_name:>s}\n"

    print(f"{header}\n{comp_pits}\n{bowls}\n{player_pits}\n{footer}")


#gets the pit selection from player and the seed count of said pit
def select_pit_take_seeds(who_has_turn):
    seeds = 0
    if who_has_turn == player:
        while seeds == 0:
            pit = input("\nPick a pit: ")
            #gets seed count or gives error message if out of range of player pits
            try:
                pit = int(pit)
                if pit > 6 or pit < 1:
                    print("Woops, you have to pick a number between 1 and 6.")
                elif pits[pit] == 0:
                    print("Sorry, that pit is empty")
                else:
                    seeds = pits[pit]
            #error message if input is non-numeric, unless input is 'rules', then shows rules
            except:
                if pit.lower() == "rules":
                    rules()
                    display()
                else:
                    print("That's not an option, please pick a number between 1 and 6.")
    else:
        print(f"\n{computer} is picking a pit...")
        while seeds == 0:
            #looking for free move, else picking random
            for i in range(8,14):
                num_to_hit_bowl = i - 7
                if pits[i] == num_to_hit_bowl:
                    pit = i
                    break
                else:
                    pit = random.randint(8,13)
            seeds = pits[pit]
    
    time.sleep(1)
    if who_has_turn == player:
        print(f"\n{who_has_turn} takes {seeds} seeds from pit {pit}.")
    else:
        print(f"\n{who_has_turn} takes {seeds} seeds from pit {str(int(pit - 7))}.")
    time.sleep(1)
    print("\nRedistributing seeds and updating gameboard...")
    time.sleep(1)
    return pit, seeds


#takes pit chosen by player/computer and updates pits dict after redistributing
def redistribute_seeds(who_has_turn, pit, seeds):
    pits.update({pit:0})
    if who_has_turn == computer:
        not_my_bowl = 0
    else:
        not_my_bowl = 7

    #distributes the seeds counter-clockwise, adding to owner's bowl if passed
    for seed in range(seeds):
        if pit - 1 < 0 or pit - 1 == not_my_bowl:
            pit = 13
            seeds_in_pit = pits[pit]
            seeds_in_pit += 1
            pits.update({pit:seeds_in_pit})
        else:
            pit -= 1
            seeds_in_pit = pits[pit]
            seeds_in_pit += 1
            pits.update({pit:seeds_in_pit})
    
    #last pit a seed was put in
    return pit


#checks if the game is over, else returns False
def game_status(pits):
    player_pits_total = 0
    comp_pits_total = 0
    for i in range(8,14):
        comp_pits_total += pits[i]
    for i in range(1,7):
        player_pits_total += pits[i]
    if comp_pits_total == 0 or player_pits_total == 0:
        return True 
    else:
        return False


#runs the game
def play_game():
    game_over = False
    who_has_turn = player
    while game_over == False:
        #turn info 
        if who_has_turn == computer and game_over == False:
            pit = 7
            bowl = 7
            pits_owned = list(range(8,14))
            opponent = player
        elif who_has_turn == player and game_over == False:
            pit = 0
            bowl = 0
            pits_owned = list(range(1,7))
            opponent = computer

        #makes move and seeds are redistributed
        while pit == bowl and game_over == False:
            move = select_pit_take_seeds(who_has_turn)
            pit = move[0]
            seeds = move[1]
            pit = redistribute_seeds(who_has_turn, pit, seeds)
            display() 

            #checks if last landing pit qualifies for taking oppenent's seeds
            if pit in pits_owned and pits[pit] == 1 and pits[op_pits[pit]] > 0:
                print(f"\n{who_has_turn} takes {pits[op_pits[pit]]} from {opponent}'s pit!")
                time.sleep(1)
                print("\nRedistributing seeds and updating gameboard...")
                time.sleep(1)
                while pit in pits_owned and pits[pit] == 1 and pits[op_pits[pit]] > 0 and game_over == False:
                    pits[pit] += pits[op_pits[pit]] 
                    pits[op_pits[pit]] = 0
                    seeds = pits[pit]
                    pit = redistribute_seeds(player, pit, seeds)
                    
                    #prevents another auto move if game over after last one
                    game_over = game_status(pits)

                display()
                
            #prevents being stuck in loop if game over before turn switch
            game_over = game_status(pits)  

            #free move message if last seed landed in the bowl
            if pit == 7 and game_over == False:
                print("\nFree move!")
                time.sleep(1)
                display()

        #ending game if over, else switching turns          
        if game_over == True:
            break
        else:
            who_has_turn = opponent


#gives the final scores and winner
def end_game():
    print("GAME OVER")
    time.sleep(1)

    player_pits_total = 0
    comp_pits_total = 0
    #gets totals from pits and empties them
    for i in range(8,14):
        comp_pits_total += pits[i]
        pits[i] = 0
    for i in range(1,7):
        player_pits_total += pits[i]
        pits[i] = 0
    #adds remaining seeds from pits to bowls
    pits[0] += player_pits_total
    pits[7] += comp_pits_total
    player_score = pits[0]
    comp_score = pits[7]

    #printing scores
    print(f"\nFinal score: {computer} {str(comp_score)} / {player} {str(player_score)}\n")
    time.sleep(1)

    #declaring winner
    if comp_score == player_score:
        print(f"{computer} and {player} tie!\n")
    else:
        if comp_score > player_score:
            winner = computer
        else:
            winner = player
        print(f"The winner is {winner}!\n")


#the seed distribution of the board
pits = {0:0, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:0, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
op_pits = {1:13, 2:12, 3:11, 4:10, 5:9, 6:8, 8:6, 9:5, 10:4, 11:3, 12:2, 13:1}
# seeds = 0
# pit = 0

#names for the players, can be changed to whatever
player = "Lorelei"
computer = "Computer"


start_message()
play_game()    
end_game()