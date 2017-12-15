from deck import Deck
from hand import Hand


def dealer(dealer_hand):
    while True:
        score = dealer_hand.score()
        if score > 21:
            print('Dealer hand: {}'.format(', '.join(str(c) for c in dealer_hand.hand)))
            return 'bust'
        elif dealer_hand.hand == dealer_hand.starting_hand and score == 21:
            print('Dealer hand: {}'.format(', '.join(str(c) for c in dealer_hand.hand)))
            return 'blackjack'
        if score >= 17:
            print('Dealer hand: {}'.format(', '.join(str(c) for c in dealer_hand.hand)))
            return score
        else:
            dealer_hand.add_card()
            continue


if __name__ == '__main__':
    d = Deck()
    d.shuffle()
    d.cut()
    d_h = Hand(d)
    print(dealer(d_h))
