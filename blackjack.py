import random
import time
import os
deck = ['A(\u2660)', 'A(\u2665)', 'A(\u2666)', 'A(\u2663)', '2(\u2660)', '2(\u2665)', '2(\u2666)', '2(\u2663)', '3(\u2660)', '3(\u2665)', '3(\u2666)', '3(\u2663)', '4(\u2660)', '4(\u2665)', '4(\u2666)', '4(\u2663)', '5(\u2660)', '5(\u2665)', '5(\u2666)', '5(\u2663)', '6(\u2660)', '6(\u2665)', '6(\u2666)', '6(\u2663)', '7(\u2660)', '7(\u2665)', '7(\u2666)', '7(\u2663)', '8(\u2660)', '8(\u2665)', '8(\u2666)', '8(\u2663)', '9(\u2660)', '9(\u2665)', '9(\u2666)', '9(\u2663)', '10(\u2660)', '10(\u2665)', '10(\u2666)', '10(\u2663)', 'J(\u2660)', 'J(\u2665)', 'J(\u2666)', 'J(\u2663)', 'Q(\u2660)', 'Q(\u2665)', 'Q(\u2666)', 'Q(\u2663)', 'K(\u2660)', 'K(\u2665)', 'K(\u2666)', 'K(\u2663)']
def calchandval(hand) -> int:
    val1 = 0
    val2 = 0
    for x in hand:
        if x[0] == "A":
            val1 += 1
            val2 += 11
        elif x[0] == "J" or x[0] == "Q" or x[0] == "K" or x[:2] == "10":
            val1 += 10
            val2 += 10
        else:
            val1 += int(x[0])
            val2 += int(x[0])
    if val2 > 21:
        val2 = 0
    return max(val1, val2)

def hit(hand, gamedeck):
    hand.append(gamedeck.pop())
    return hand, gamedeck

def displayhandvalue(player_hand, dealer_hand, finish):
    if finish:
        print(f"Dealer Hand: {dealer_hand} Value: {calchandval(dealer_hand)}")
        print(f"Player Hand: {player_hand} Value: {calchandval(player_hand)}")
    else:
        print(f"Dealer Hand: {dealer_hand[0]} + ? Value: {calchandval(dealer_hand[:1])}")
        print(f"Player Hand: {player_hand} Value: {calchandval(player_hand)}")

def gamecontinue():
    cmd = input("Type R or play again or Q to quit.")
    while True:
        if cmd.lower() == "q":
            quit()
        elif cmd.lower() == "r":
            return True
        else:
            cmd = input("Invalid Input, Type R or play again or Q to quit.")

def aiturn(dealer_hand, player_hand, gamedeck):
    while calchandval(dealer_hand) < 16:
        dealer_hand, gamedeck = hit(dealer_hand, gamedeck)
        displayhandvalue(player_hand, dealer_hand, True)
        time.sleep(2)

    if calchandval(dealer_hand) > 22:
        print("You Win")
        return gamecontinue()
    else:
        displayhandvalue(player_hand, dealer_hand, True)
        if calchandval(player_hand) > calchandval(dealer_hand):
            print("You Win")
            return gamecontinue()
        elif calchandval(player_hand) < calchandval(dealer_hand):
            print("You Lose")
            return gamecontinue()
        else:
            print("Tie")
            return gamecontinue()
    
    

def game():
    coninues = True
    while coninues:
        gamedeck = deck
        random.shuffle(gamedeck)
        dealer_hand = []
        player_hand = []
        gameover = False
        
        #setting up the hand
        dealer_hand.append(gamedeck.pop())
        player_hand.append(gamedeck.pop())
        player_hand.append(gamedeck.pop())
        dealer_hand.append(gamedeck.pop())
        print("Dealer will always stay after getting a number above 16, and will always hit if they are below or equal to 16")
        displayhandvalue(player_hand, dealer_hand, False)
        cmd = input("Type H or hit or S to stand.")
        while True:
            if cmd.lower() == "h":
                player_hand, gamedeck = hit(player_hand, gamedeck)
                os.system('cls' if os.name == 'nt' else 'clear')
            elif cmd.lower() == "s":
                break
            else:
                cmd = input("Invalid Input. Type H or hit or S to stand.")
            displayhandvalue(player_hand, dealer_hand, False)
            if calchandval(player_hand) > 21:
                print("You Lose")
                displayhandvalue(player_hand, dealer_hand, True)
                gameover = True
                break
            cmd = input("Invalid Input. Type H or hit or S to stand.")
        if gameover:
            coninues = gamecontinue()
        else:
            coninues = aiturn(dealer_hand, player_hand, gamedeck)

def main() -> None:
    game()

if __name__ == '__main__':
    main()
