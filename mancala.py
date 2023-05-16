import os
import time
import random

def display(name):
    os.system('cls')
    title = "__Mancala__"
    player_pit_lables = "6       5       4       3       2       1"
    comp_pit_lables = "8       9       10      11      12      13"
    comp_name = "Computer"
    player_name = name
    vs = "--vs--"
    vs_space = 64 - len(comp_name) - len(player_name)
    header = f"{title:^64s}\n{comp_pit_lables:^64s}"
    comp_pits = f"        ({pits[8]:^5d}) ({pits[9]:^5d}) ({pits[10]:^5d}) ({pits[11]:^5d}) ({pits[12]:^5d}) ({pits[13]:^5d})"
    bowls = f"({pits[7]:^5d})                                                 ({pits[0]:^5d})"
    player_pits = f"        ({pits[6]:^5d}) ({pits[5]:^5d}) ({pits[4]:^5d}) ({pits[3]:^5d}) ({pits[2]:^5d}) ({pits[1]:^5d})"
    footer = f"{player_pit_lables:^64s}\n{comp_name:<s}{vs:^{vs_space}s}{player_name:>s}\n"

    print(f"{header}\n{comp_pits}\n{bowls}\n{player_pits}\n{footer}")

def player_takes_seeds():
    seeds = 0
    # print(pits)
    while seeds == 0:
        try:
            pit = int(input("\nPick a pit: "))
            if pit == 0:
                print("That's your bowl. Those seeds stay there.")
            elif pit > 6:
                print("That's not your pit...")
            elif pits[pit] == 0:
                print("Sorry, that pit is empty")
            else:
                seeds = pits[pit]
        except:
            print("That's not an option, please pick a number between 1 and 6.")
    time.sleep(1)
    print(f"\nPlayer takes {seeds} seeds from pit {pit}.")
    time.sleep(1)
    print("\nRedistributing seeds and updating gameboard...")
    time.sleep(1)
    return pit, seeds

def comp_takes_seeds():
    seeds = 0
    # print(pits)
    print("Computer is picking a pit...")
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
    print(f"\nComputer takes {seeds} seeds from pit {pit}.")
    time.sleep(1)
    print("\nRedistributing seeds and updating gameboard...")
    time.sleep(1)
    # print(f"seeds: {seeds}, pit: {pit}")
    return pit, seeds

def redistribute_seeds(player_name, pit, seeds):
    pits.update({pit:0})
    if player_name == "computer":
        not_my_bowl = 0
    else:
        not_my_bowl = 7

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
    return pit

def auto_move(player_name, pit):
    seeds = pits[pit]
    pits.update({pit:0})
    if player_name == "computer":
        not_my_bowl = 0
    else:
        not_my_bowl = 7

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
    return pit

def play_game():
    game_over = False
    turn = player
    while game_over == False:
        if turn == computer and game_over == False:
            pit = 7
            while pit == 7 and game_over == False:
                comp_move = comp_takes_seeds() 
                pit = comp_move[0]
                seeds = comp_move[1]
                pit = redistribute_seeds(computer, pit, seeds)
                display(player) 

                if pit >= 8 and pits[pit] == 1 and pits[op_pits[pit]] > 0:
                    print("Auto move!")
                    time.sleep(1)
                    while pit >= 8 and pits[pit] == 1 and pits[op_pits[pit]] > 0 and game_over == False:
                        pits[pit] += pits[op_pits[pit]] 
                        pits[op_pits[pit]] = 0
                        pit = auto_move(computer, pit)
                        
                        #checking if player or computer pits are empty, therefore game_over == True
                        player_pits_total = 0
                        comp_pits_total = 0
                        for i in range(8,14):
                            comp_pits_total += pits[i]
                        for i in range(1,7):
                            player_pits_total += pits[i]
                        if comp_pits_total == 0 or player_pits_total == 0:
                            game_over = True

                    display(player)
                    
                #checking if player or computer pits are empty, therefore game_over == True
                player_pits_total = 0
                comp_pits_total = 0
                for i in range(8,14):
                    comp_pits_total += pits[i]
                for i in range(1,7):
                    player_pits_total += pits[i]
                if comp_pits_total == 0 or player_pits_total == 0:
                    game_over = True    

            #breaking if game_over == True, else switching turns            
            if game_over == True:
                break
            else:
                turn = player

        elif turn == player and game_over == False:
            pit = 0
            while pit == 0 and game_over == False:
                play_move = player_takes_seeds()
                pit = play_move[0]
                seeds = play_move[1]
                pit = redistribute_seeds(player, pit, seeds)
                display(player)
                seeds_remaining = 0
                
                if pit > 0 and pit <= 6 and pits[pit] == 1 and pits[op_pits[pit]] > 0:
                    print("Auto move!")
                    time.sleep(1)
                    while pit > 0 and pit <= 6 and pits[pit] == 1 and pits[op_pits[pit]] > 0 and game_over == False:
                        pits[pit] += pits[op_pits[pit]] 
                        pits[op_pits[pit]] = 0
                        pit = auto_move(player, pit)

                        #checking if player or computer pits are empty, therefore game_over == True
                        player_pits_total = 0
                        comp_pits_total = 0
                        for i in range(8,14):
                            comp_pits_total += pits[i]
                        for i in range(1,7):
                            player_pits_total += pits[i]
                        if comp_pits_total == 0 or player_pits_total == 0:
                            game_over = True

                    display(player)

                #checking if player or computer pits are empty, therefore game_over == True
                player_pits_total = 0
                comp_pits_total = 0
                for i in range(8,14):
                    comp_pits_total += pits[i]
                for i in range(1,7):
                    player_pits_total += pits[i]
                if comp_pits_total == 0 or player_pits_total == 0:
                    game_over = True    

            #breaking if game_over == True, else switching turns            
            if game_over == True:
                break
            else:
                turn = computer

        #breaking out of play loop to end the game        
        else:
            break


def end_game():
    print("GAME OVER")
    time.sleep(1)

    #getting scores
    player_pits_total = 0
    comp_pits_total = 0
    for i in range(8,14):
        comp_pits_total += pits[i]
    for i in range(1,7):
        player_pits_total += pits[i]
    player_score = player_pits_total + pits[0]
    comp_score = comp_pits_total + pits[7]

    #declairing winner
    if comp_score > player_score:
        winner = computer
    elif comp_score < player_score:
        winner = player
    else:
        winner = "no one"
    print(f"\nFinal score: {str(comp_score)}/{str(player_score)}\n")
    time.sleep(1)
    print(f"The winner is {winner}!\n")

pits = {0:0, 1:4, 2:4, 3:4, 4:4, 5:4, 6:4, 7:0, 8:4, 9:4, 10:4, 11:4, 12:4, 13:4}
op_pits = {1:13, 2:12, 3:11, 4:10, 5:9, 6:8, 8:6, 9:5, 10:4, 11:3, 12:2, 13:1}
seeds = 0
pit = 0

player = "Lorelei"
computer = "computer"
turn = player

display(player) #WORKING
play_game()    
end_game()