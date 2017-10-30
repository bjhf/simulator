from .enum import *


def get_card_text(card):
    output = ''
    if card & Card.ACE:
        output += 'A'
    elif card & Card.TWO:
        output += '2'
    elif card & Card.THREE:
        output += '3'
    elif card & Card.FOUR:
        output += '4'
    elif card & Card.FIVE:
        output += '5'
    elif card & Card.SIX:
        output += '6'
    elif card & Card.SEVEN:
        output += '7'
    elif card & Card.EIGHT:
        output += '8'
    elif card & Card.NINE:
        output += '9'
    elif card & Card.TEN:
        output += 'T'
    elif card & Card.JACK:
        output += 'J'
    elif card & Card.QUEEN:
        output += 'Q'
    elif card & Card.KING:
        output += 'K'
    if card & Card.SPADE:
        output += 's'
    elif card & Card.DIAMOND:
        output += 'd'
    elif card & Card.CLUB:
        output += 'c'
    elif card & Card.HEART:
        output += 'h'
    return output

def get_card_value(card):
    if card & Card.ACE:
        if card & Card.ISHIGH:
            return 11
        return 1
    if card & Card.TWO:
        return 2
    if card & Card.THREE:
        return 3
    if card & Card.FOUR:
        return 4
    if card & Card.FIVE:
        return 5
    if card & Card.SIX:
        return 6
    if card & Card.SEVEN:
        return 7
    if card & Card.EIGHT:
        return 8
    if card & Card.NINE:
        return 9
    if card & Card.TEN:
        return 10
    if card & Card.JACK:
        return 10
    if card & Card.QUEEN:
        return 10
    if card & Card.KING:
        return 10
    return -1

def print_cards(cards):
    for card in cards:
        print(get_card_text(card), end=' ')
