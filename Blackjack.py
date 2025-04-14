import random
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def player_initial_cards():
    card1 = random.randint(2, 11)
    card2 = random.randint(2, 11)
    print(f"Your cards are: [{card1}] [{card2}]")
    global player_sum
    player_sum = card1 + card2
    if card1 == 11 and player_sum > 21:
        card1 = 1
    if card2 == 11 and player_sum > 21:
        card2 = 1
    player_sum = card1 + card2
    print("Your total is:", player_sum)
    print("\n")
    return player_sum

def computer_initial_cards():
    card1 = random.randint(2, 11)
    card2 = random.randint(2, 11)
    print("Computer's cards are: [#] [#]")
    global computer_sum
    global player_sum
    computer_sum = card1 + card2
    if card1 == 11 and computer_sum > 21:
        card1 = 1
    if card2 == 11 and computer_sum > 21:
        card2 = 1
    computer_sum = card1 + card2
    print("Computer's total is: #")
    print("\n")
    if player_sum == 21:
        print("You won with", player_sum)
    elif computer_sum == 21:
        print("Computer won with", computer_sum)
    elif player_sum >= 16:
        print("\n-------Player's turn-------\n")
        choice = input("Do you want to reveal your cards? y(Yes) or n(No)\n")
        if choice == "y":
            print("Your total:", player_sum)
            print("Computer's total:", computer_sum)
            if player_sum > computer_sum:
                print("Player wins with:", player_sum)
                return False
            elif player_sum == computer_sum:
                print("It's a draw with:", player_sum)
                return False
            else:
                print("You lost, computer wins with:", computer_sum)
                return False
    return computer_sum

def hit_or_stand_player():
    choice = input("Do you want to draw a card? h(Hit) or s(Stand)\n")
    if choice == "h":
        new_card = random.randint(2, 11)
        print(f"New card: [{new_card}]")
        global player_sum
        global computer_sum
        player_sum += new_card
        if player_sum > 21:
            print("You lost with a total of:", player_sum)
            print("Too bad...")
            return False
        elif player_sum == 21:
            print("You won with:", player_sum)
            print("Congratulations!")
            return False
        else:
            print("Your new total is:", player_sum)
            return True
    elif choice == "s":
        print("Your total remains:", player_sum)
        return player_sum
    else:
        print("Please enter a valid option: h or s")
        return True

def blackjack():
    print("---------------Game Start--------------")
    print("----------------Player's Turn--------------\n")
    player_initial_cards()
    print("--------------Computer's Turn------------\n")
    result = computer_initial_cards()
    if result == False:
        return
    print("-------Player's Turn-------\n")
    while True:
        if not hit_or_stand_player():
            break
        print("-------Computer's Turn-------\n")
        global computer_sum
        global player_sum
        if computer_sum < 19:
            print("Computer draws a card")
            new_card = random.randint(2, 11)
            print("Card is: [#]")
            computer_sum += new_card
            if computer_sum > 21:
                print("Computer lost with a total of:", computer_sum)
                print("You win, congratulations!")
                break
            elif computer_sum == 21:
                print("Computer wins with:", computer_sum)
                break
        else:
            print("Computer decided to stand with: #")
        print("Computer's total: #")

def game_loop():
    while True:
        time.sleep(3)
        clear_console()
        print("-----------------Welcome----------------")
        choice = input("Do you want to play Blackjack/21? y(Yes) or n(No)\n")
        if choice == "y":
            blackjack()
        elif choice == "n":
            print("Maybe next time...")
            break
        else:
            print("Please write correctly! Only y or n allowed.")

game_loop()
