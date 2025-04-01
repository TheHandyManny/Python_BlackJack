import random

# Constants
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
          '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}


def create_deck():
    #Create deck using list comprehension with a nested for loop
    return [{'Rank': rank, 'Suit': suit} for rank in ranks for suit in suits]

def shuffle_deck(deck):
    #Reorganize deck using Random module
    random.shuffle(deck)

# Calculate hand total with Ace handling
def calculate_total(hand):
    #Grabs values of cards and sums it up using a built in python module: sums. Sums iterates over iterable objects and sums it up. So the following list comprehension gets the values of the cards and passes it as a list into sum().
    total = sum(values[card['Rank']] for card in hand)

    #Sets the total number of aces in hand for use later
    aces = sum(1 for card in hand if card['Rank'] == 'A')
    
    #Loop that Reduces hand value per each ace
    while total > 21 and aces:
        total -= 10
        aces -= 1
    return total

# Prints card details from hand.
def display_hand(name, hand, hide_second=False):
    if hide_second:
        print(f"{name}'s hand: [{hand[0]['Rank']} of {hand[0]['Suit']}, Hidden]")
    else:
        hand_str = ', '.join(f"{card['Rank']} of {card['Suit']}" for card in hand)
        print(f"{name}'s hand: [{hand_str}]")

# Main game
def play_blackjack():
    deck = create_deck()
    shuffle_deck(deck)

    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand, hide_second=True)

    # Player turn
    while True:
        player_total = calculate_total(player_hand)
        print(f"Player total: {player_total}")
        choice = input("Hit or Stand? ").strip().lower()
        
        if choice == 'hit':
            card = deck.pop()
            player_hand.append(card)
            player_total = calculate_total(player_hand)
            print("You drew:", card['Rank'], "of", card['Suit'])
            if player_total > 21:
                print(f"Player total after hit: {player_total}")
                print("You busted! Dealer wins.")
                display_hand("Player", player_hand)
                display_hand("Dealer", dealer_hand)
                return
        elif choice == 'stand':
            break
        else:
            print("Invalid input. Please type 'Hit' or 'Stand'.")

    # Dealer turn
    print("\nDealer's turn:")
    display_hand("Dealer", dealer_hand)
    dealer_total = calculate_total(dealer_hand)
    
    while dealer_total < 16:
        card = deck.pop()
        dealer_hand.append(card)
        print("Dealer drew:", card['Rank'], "of", card['Suit'])
        dealer_total = calculate_total(dealer_hand)

    player_total = calculate_total(player_hand)
    dealer_total = calculate_total(dealer_hand)

    print(f"\nFinal Totals -> Player: {player_total} | Dealer: {dealer_total}")
    display_hand("Player", player_hand)
    display_hand("Dealer", dealer_hand)

    if dealer_total > 21 or player_total > dealer_total:
        print("You Win!")
    elif dealer_total > player_total:
        print("You Lose.")
    else:
        print("It's a Tie.")

# Run the game
play_blackjack()
