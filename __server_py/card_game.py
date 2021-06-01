# Two useful variables for creating Cards.
from random import shuffle
from string import capwords


SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q H A'.split()

my_cards = [(s, r) for s in SUITE for r in RANKS]

# my_cards_test = []
# for r in RANKS:
#     for s in SUITE:
#         my_cards_test.append((s, r))

# print(my_cards)
# print(my_cards_test)


class Deck:
    def __init__(self) -> None:
        print('Create New Ordered Deck!')
        self.allcards = my_cards

    def shuffle(self):
        print('SHUFFLING DECK')
        shuffle(self.allcards)

    def spilt_in_half(self):
        # return (self.allcards[:26], self.allcards[26:])
        half = len(self.allcards)//2
        return (self.allcards[:half], self.allcards[half:])


class Hand:
    def __init__(self, cards) -> None:
        self.cards = cards

    def __str__(self) -> str:
        return "Contains {} cards".format(len(self.cards))

    def add(self, add_cards):
        self.cards.extend(add_cards)

    def remove_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name, hand) -> None:
        self.name = name
        self.hand = hand

    def paly_card(self):
        drown_card = self.hand.remove_card()
        print('{} has placed: {}'.format(self.name, drown_card))
        print('\n')
        return drown_card

    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards

        for x in range(3):
            # war_cards.append(self.hand.cards.pop())
            war_cards.append(self.hand.remove_card())
        return war_cards

    def still_have_cards(self):
        return len(self.hand.cards)


print("Welcome to War, let's begin...")
# Create new deck and split it in half
d = Deck()
d.shuffle()
half1, half2 = d.spilt_in_half()

# Create both players!
comp = Player('computer', Hand(half1))

name = input('what is your name?')
user = Player(name, Hand(half2))

total_rounds = 0
war_count = 0


def battle():
    if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
        user.hand.add(table_cards)
    else:
        comp.hand.add(table_cards)


while user.still_have_cards() and comp.still_have_cards():
    total_rounds += 1
    print('Time for a new round!')
    print('here are the current standings')
    print(user.name+'has the count: '+str(len(user.hand.cards)))
    print(comp.name+'has the count: '+str(len(comp.hand.cards)))
    print('play a card!')
    print('\n')

    table_cards = []

    c_card = comp.paly_card()
    p_card = user.paly_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print('war!')

        table_cards.extend(comp.remove_war_cards())
        table_cards.extend(user.remove_war_cards())

        battle()
    else:
        battle()

print('game over, number of rounds: ' + str(total_rounds))
print('a war happened: '+str(war_count)+' times')

print('Does the computer still have cards? ')
print(str(comp.still_have_cards()))
print('Does the player still have cards? ')
print(str(user.still_have_cards()))
