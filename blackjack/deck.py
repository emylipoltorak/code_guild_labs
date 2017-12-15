from playing_card import Card
import uuid
import random

suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']


class Deck:
    def __init__(self):
        self.deck_id = str(uuid.uuid4())[:4]
        self.cards = self.build_deck()

    def build_deck(self):
        deck = []
        for suit in suits:
            for rank in ranks:
                deck.append(Card(suit, rank, self.deck_id))
        return deck

    def shuffle(self):
        return random.shuffle(self.cards)

    def cut(self):
        cut_int = random.randint(20, 30)
        self.cards = self.cards[cut_int:]+self.cards[:cut_int]
        return self.cards

    def draw(self):
        return self.cards.pop(0)



    def __repr__(self):
        repr_cards = []
        for c in self.cards:
            repr_cards.append(repr(c))
        return '-'.join(repr_cards)

    def __str__(self):
        str_cards = []
        for c in self.cards:
            str_cards.append(str(c))
        return ', '.join(str_cards)


if __name__ == '__main__':

    d = Deck()
    for x in range(53):
        print(d.draw())
