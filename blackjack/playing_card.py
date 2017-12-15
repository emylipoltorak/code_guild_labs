class Card:
    def __init__(self, suit, rank, deck_id):
        self.suit = suit
        self.rank = rank
        self.deck_id = deck_id
        self.value = self.get_value()

    def get_value(self):
        try:
            return int(self.rank)
        except ValueError:
            if self.rank in 'JQK':
                return 10
            elif self.rank is 'A':
                return 11

    def __str__(self):
        royalty = {'A': 'Ace', 'K': 'King', 'Q': 'Queen', 'J': 'Jack'}
        try:
            return '{} of {}'.format(royalty[self.rank], self.suit)
        except KeyError:
            return '{} of {}'.format(self.rank, self.suit)

    def __repr__(self):
        return '{}{}'.format(self.rank[0], self.suit[0])
