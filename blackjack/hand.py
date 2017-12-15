from deck import Deck


class Hand:
    def __init__(self, deck):
        self.deck = deck
        self.starting_hand = self.assign_starting_hand()
        self.hand = self.starting_hand[:]

    def assign_starting_hand(self):
        self.starting_hand = []
        for i in range(2):
            self.starting_hand.append(self.deck.draw())
        return self.starting_hand

    def add_card(self):
        card = self.deck.draw()
        self.hand.append(card)
        return self.hand

    def score(self):
        score = 0
        for c in self.hand:
            score += c.value
        num_aces = len([x for x in self.hand if x.rank is 'A'])
        while num_aces:
            if score > 21:
                score -= 10
                num_aces -= 1
            else:
                break
        return score

    def __str__(self):
        return 'Your hand is: {}.'.format(', '.join(str(c) for c in self.hand))


if __name__ == '__main__':
    d = Deck()
    d.shuffle()
    d.cut()
    # print(d.cards[:2])

    h = Hand(d)
    print(h)
    h.add_card()
    print(h)
    h.add_card()
    print(h)
