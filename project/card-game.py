import random
import sys


class Card:
    suits = [
        "\u2666",
        "\u2665",
        "\u2663",
        "\u2660",
    ]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    def __init__(self, suit=0, rank=0):
        """Default constructor"""
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Returns a human-readable string representation"""
        return "%s %s" % (Card.suits[self.suit], Card.ranks[self.rank])

    def __lt__(self, other):
        """Overriding < operator"""
        t1 = self.rank, self.suit
        t2 = other.rank, other.suit
        return t1 < t2


class Deck:
    def __init__(self):
        """Initializes the Deck with 52 cards."""
        self.cards = []
        for suit in range(4):
            for rank in range(13):
                card = Card(suit, rank)
                self.cards.append(card)
        self.shuffle()

    def __str__(self):
        """Returns a string representation of the deck."""
        res = []
        for card in self.cards:
            res.append(str(card))
        return ", ".join(res)

    def __len__(self):
        """Overriding len operator"""
        return len(self.cards)

    def add_card(self, card):
        """Adds a card to the deck."""
        self.cards.append(card)

    def pop_card(self, i=-1):
        """Removes and returns a card from the deck.
        i: index of the card to pop; by default, pops the last card.
        """
        return self.cards.pop(i)

    def shuffle(self):
        """Shuffles the cards in this deck."""
        random.shuffle(self.cards)

    def sort(self):
        """Sorts the cards in ascending order."""
        self.cards.sort()

    def wincard(self, cards):
        """Get the highest winner card from list"""
        winner = cards[0]
        for card in cards:
            if winner < card:
                winner = card
        return winner


class Hand(Deck):
    """
    Represents a hand of playing cards.
    """

    def __init__(self, label=""):
        self.cards = []
        self.label = label
        self.wincount = 0

    def getlabel(self):
        return self.label

    def roundwinner(self):
        self.wincount += 1

    def getwincount(self):
        return self.wincount

    def __str__(self):
        return "Card for " + self.label + " is " + Deck.__str__(self)


def play(argv):
    deck = Deck()
    hands = []
    for i in range(1, 5):
        player = "Player %d" % i
        if len(argv) > i:
            player = argv[i]
        hands.append(Hand(player))

    while len(deck) > 0:
        for hand in hands:
            hand.add_card(deck.pop_card())

    print(hands[0])
    input(
        "Lets start playing. Press any key to continue : "
    )  # wait for keypress

    for i in range(1, 14):
        cards = []
        floors = []
        for hand in hands:
            card = hand.pop_card()
            cards.append(card)
            floors.append(hand.getlabel() + " : " + str(card))

        winner_card = deck.wincard(cards)
        winner_hand = hands[cards.index(winner_card)]
        winner_hand.roundwinner()
        print(
            "Round",
            i,
            ":-",
            ", ".join(floors),
            ", Winner :- ",
            winner_hand.getlabel(),
            ":",
            winner_card,
        )
        input()

    for hand in hands:
        print("Score for", hand.getlabel(), "is", hand.getwincount())


def main(argv=[]):
    answer = "Y"
    while answer.upper() == "Y":
        play(argv)
        answer = input("Play Again (Y/N)? : ")
    print("Bye Bye")


if __name__ == "__main__":
    main(sys.argv)
