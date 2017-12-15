from dealer import *


def new_game(players=1, d=Deck()):
    d.shuffle()
    d.cut()
    d_hand = Hand(d)
    p_hands = [Hand(d) for x in range(players)]
    return d, d_hand, p_hands


def evaluate_hand(h):
    print(h)
    score = h.score()
    if score > 21:
        print('{}: Bust'.format(score))
        return 'bust'
    elif h.hand == h.starting_hand and score == 21:
        print('21: Blackjack!')
        return 'blackjack'
    else:
        return act(h)


def act(h):
    choice = input(
        'Your score is {}. What would you like to do? H for hit or S for stay: '.format(h.score())).lower()
    if choice in 'hit':
        try:
            h.add_card()
        except IndexError:
            print('Deck is empty')
            exit()
        return evaluate_hand(h)
    else:
        return h.score()


def winnings(d_final_hand, f_h, bet=10):
    if f_h == 'bust':
        return 'You have lost this hand, and your bet of ${}.'.format(bet)
    elif f_h == d_final_hand:
        return 'Tie! No money changes hands.'
    elif d_final_hand == 'blackjack':
        return 'You have lost this hand, and your bet of ${}.'.format(bet)
    elif f_h == 'blackjack':
        return 'Blackjack! You have won this round! You won ${}!'.format(int(bet * 1.5))
    elif d_final_hand == 'bust' or f_h > d_final_hand:
        return 'You have won this round! You won ${}!'.format(bet)
    else:
        return 'You have lost this hand, and your bet of ${}'.format(bet)


def game_loop(players=1):
    current_game = new_game(players)
    d = current_game[0]
    while True:
        d_hand = current_game[1]
        p_hands = current_game[2]
        p_final_hands = []
        query = input('Press enter to play a hand of blackjack, or Q to quit: '.lower())
        if query == '':
            print('The dealer\'s face-up card is {}.'.format(d_hand.hand[0]))
            for h in p_hands:
                print('Player {}:'.format(p_hands.index(h)+1))
                p_final_hands.append(evaluate_hand(h))
            d_final_hand = dealer(d_hand)
            print('Dealer: {}'.format(d_final_hand))
            for f_h in p_final_hands:
                print('Player {}:'.format(p_final_hands.index(f_h) + 1))
                print(winnings(d_final_hand, f_h))
            try:
                current_game = new_game(players, d)
            except IndexError:
                print('The deck is empty')
                exit()
            continue
        elif query == 'q':
            exit()
        else:
            print('That is not a valid entry.')
            continue


if __name__ == '__main__':
    game_loop()
