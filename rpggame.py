#Name- Abhash Niroula
#Class - CS 195
#Student ID - 443015

import random
CREATURES = ('monster', 'rabbit', 'fox', 'rat')
ITEMS = ('helmet','shield', 'boots', 'chest plate', 'gauntlets')
OTHER_THINGS  = ('bush', 'big tree', 'rock')
ALL_THINGS = CREATURES + ITEMS + OTHER_THINGS

cur_health = 20
user_Items=()
coins = 0


while True:
    print("\033[H\033[2J", end="")
    print("Welcome to the 'GRAND RPG' game created by Abhash.\n")
    current =print(f'current health :{cur_health}       coins:{coins}         numberofitems:{len(user_Items)}\n')
    #print(f"The total items you collected are {user_Items}\n")
    print("The total items you collected are", end = " ")
    print(', '.join(str(x) for x in user_Items))
    rand_Thing =  random.choice(ALL_THINGS) 
    #print(rand_Thing)
    if rand_Thing in ITEMS and rand_Thing not in user_Items:
        
        '''print("The total items you collected are displayed below:")
        for item in user_Items:
            print(f"*{item}")'''

        print(f"\nALERT!!!\n{rand_Thing} came in between you and your destination. Do you want to pick it up? (Y for yes and N for no)")
        choice = input()
        if choice != "N".lower():
            user_Items += (rand_Thing,)
            continue

    elif rand_Thing in CREATURES:
        if rand_Thing == "monster":
            at_Amount = 7 - len(user_Items)#number of armor items
            print(f"\nYou encountered monster and were attacked by {at_Amount}.")
            cur_health -= at_Amount      
        else:
            print(f"\nYou encountered a {rand_Thing}.")  

        fight = input("Do you want to fight it? (Y for yes and N for no)\n")
        if fight != "N".lower():
            if rand_Thing == "monster":
                coins += 10
                #print(f"You killed the {rand_Thing}.")

            else:
                coins += 1
                #print(f"You killed the {rand_Thing}.")
        if cur_health <= 0:
            print("You lost. Better luck next time.")
            break  
        if coins >= 100:
            print("You win.") 
            break
    else:
        print(f"\nYou have encountered a {rand_Thing}.")
        play = input("Press ENTER if you want to keep walking\n")
        if play =="ENTER".lower():
            continue


        

    
    

        



