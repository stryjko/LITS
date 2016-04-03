
_author_ = 'maryan_partyka & dima_lakh'

import random


# Creating the cards
class Card:

    mastj_list = ["Hresta", "Bubna", "Cherva", "Pika"]
    karta_list = ["2", "3", "4", "5", "6", "7", "8", "9", "10",
                  "Jack", "Queen", "King", "Ace"]

    def __init__ (self, mastj, karta):
        self.mastj = mastj
        self.karta = karta

    # string interpretation of Cards
    def __str__(self):
        return self.karta_list[self.karta] + " of " + self.mastj_list[self.mastj]

    def __cmp__(self, other):
        #check the karts
        if self.karta > other.karta:
            return 1
        if self.karta < other.karta:
            return -1
        #check the mastj
        if self.mastj > other.mastj:
            return 1
        if self.mastj < other.mastj:
            return -1
        return 0


# Creating a Deck of Cards
class Deck:

    def __init__(self):
        self.cards = []
        for mastj in range(4):
            for karta in range(13):
                self.cards.append(Card(mastj, karta))

    # string manipulation for good visual perception
    def __str__(self):
        s = ""
        for i in range(0, len(self.cards)):
            s = s + " " + str(self.cards[i]) + "\n" if (i+1) % 5 == 0 else s + " " + str(self.cards[i]) + ", "
        return s

    # Method that prints the Deck of Cards
    def print_deck(self):
        for card in self.cards:
            print card

    # Shuffling the Deck of Cards
    def shuffle(self):
        random.shuffle(self.cards)

    # Pop the Cards
    def pop_card(self):
        return self.cards.pop()

    # Remove the Cards
    def remove_card(self, card):
        if card in self.cards:
            self.cards.remove(card)
            return True
        else:
            return False

    # Check the Deck of Cards
    def is_empty(self):
        return len(self.cards) == 0

    # Dealing the Cards
    def deal(self, hands, num_cards=52):
        num_hands = len(hands)
        for i in range(num_cards):
            if self.is_empty():
                break
            card = self.pop_card()
            h = hands[i % num_hands]
            h.add_card(card)


# Players
class PlayerHand(Deck):

    def __init__(self, name=""):
            self.cards = []
            self.name = name

    def __str__(self):
        s = "Hand of Player " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self) + '\n'

    def add_card(self, card):
        self.cards.append(card)


# A hand of player for this game requires some abilities beyond the general abilities of a PlayerHand
class SpecialFunctionsPlayerHand(PlayerHand):

    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.mastj, card.karta)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print "Hand of Player %s: %s matches %s" % (self.name, card, match)
                count += 1
        return count


# start the Game :)
class OldMaidGame:

    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

    def play(self, names):
        # remove Queen of Hresta
        self.deck.remove_card(Card(0, 10))
        self.hands = []

        # make a hand for each player
        for name in names:
            self.hands.append(SpecialFunctionsPlayerHand(name))

        # deal the cards
        self.deck.deal(self.hands)
        print "\n ---------- Cards have already dealt \n"
        self.print_hands()

        # remove initial matches
        matches = self.remove_all_matches()
        print "\n ---------- All Matches were discarded \n"
        self.print_hands()
        raw_input("--------- Press <enter> to begin play a game")

        # start the play until all 50 cards are matched
        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches = matches + self.play_one_turn(turn, names)
            # variable turn is means which player will be next
            turn = (turn + 1) % num_hands

        print "------------ Game over"
        self.print_hands()

    # remove all matched cards
    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count = count + hand.remove_matches()
        return count

    # method which is count the number of matches made during this one turn
    def play_one_turn(self, i, names):
        if self.hands[i].is_empty():
            return 0
        # define your neighbor
        neighbor = self.find_neighbor(i)
        if i == names.index(names[-1]):
            print '-----------------------------------\n'
            raw_input("Now is your next turn. Press <enter> to continue")
        # get the card from the neighbor
        picked_card = self.hands[neighbor].pop_card()
        self.hands[i].add_card(picked_card)
        print "Hand", self.hands[i].name, "picked", picked_card
        # checking for matches
        count = self.hands[i].remove_matches()
        print self.hands[i]
        #  the cards in the hand will be shuffle
        self.hands[i].shuffle()
        return count

    # method find the first left player and continues around the circle
    # until it finds a player that still has cards
    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next_neighbor in range(1, num_hands):
            neighbor = (i + next_neighbor) % num_hands
            if not self.hands[neighbor].is_empty():
                return neighbor

    def print_hands(self):
        for hand in self.hands:
            print hand


def main():
    print 'Text Card Game - "Old Maid"'
    print "Official rules: \n" \
          "1. Two or more players start with a shuffled deck from which the Queen of Hresta has been removed.\n" \
          "So we have 51 cards now.\n" \
          "2. All cards are dealt in normal way; depending on the number of players, some may have one more card than others.\n" \
          "3. Players match the cards in their hands and discard all matches.\n" \
          "A match is defined as two cards of the same 'karta', whose 'mastj' is the same color.\n" \
          "4. After all matches have been discarded, each player in turn selects one card, without looking \n" \
          "from the closest neighbor to the left that who still has cards. \n" \
          "If the card matches one in the players hand, the pair is discarded. \n" \
          "Otherwise, the card is added to the hand.\n" \
          "5. Play continues until only one card remains in any hand - Queen of Pika (which is no match)\n" \
          "and that player will be the Old Maid :)\n"

    game = OldMaidGame()
    you = raw_input("What is Your name lucky player? :) - ")
    game.play(["Vasylko", "Ivasyk", "Marijka", you])

main()
