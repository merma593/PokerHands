'''
COSC326 Etude 4

Takes an input and determines if it is a valid poker hand.
If it is valid it will print, otherwise prints Invalid and the input.

@author Markham Meredith

'''
import sys
import re
from textwrap import wrap


cards = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "J", "Q", "K", "A", "T"]
suits = ["C", "D", "H", "S"]
ranks = ["2C", "2D", "2H", "2S", "3C", "3D", "3H", "3S", "4C", "4D", "4H", "4S", "5C", "5D", "5H", "5S", "6C", "6D",
         "6H", "6S", "7C", "7D", "7H", "7S", "8C", "8D", "8H", "8S", "9C", "9D", "9H", "9S", "10C", "10D", "10H", "10S",
         "JC", "JD", "JH", "JS", "QC", "QD", "QH", "QS", "KC", "KD", "KH", "KS", "AC", "AD", "AH", "AS"]


def can_split(hand):
    # Checks if input can be split into 5 chunks.
    if hand.count("/") == 4:
        split = True
    elif hand.count("-") == 4:
        split = True
    elif hand.count(" ") == 4:
        split = True
    else:
        split = False
    return split


def valid_hand(hand):
    # checks each chunk and sees if valid cards, also checks length of chunk
    valid_count = 0
    valid_nums = [str(x) for x in range(4)]
    if len(hand) != len(set(hand)):  # checks for duplicates in hand.
        return False
    else:
        for card in hand:
            if len(card) == 2:
                valid = True if card[0] in cards and card[1] in suits else False
                if valid is True:
                    valid_count += 1
            elif len(card) == 3:
                valid = True if card[0] in cards and card[1] in valid_nums and card[2] in suits else False
                if valid is True:
                    valid_count += 1
            elif len(card) > 3 or len(card) < 2:
                return False
    if valid_count == 5:
        return True
    else:
        return False


def replace(hand):
    # Replaces 1,T,11,12,13 with A,10,J,Q,K.
    new_hand = ""
    valid_cards = []

    for card in hand:
        if len(card) == 2 and card[0] == "1":
            card = card.replace("1", "A")
        elif len(card) == 2 and card[0] == "T":
            card = card.replace("T", "10")
        elif len(card) == 3:
            if card[0] == "1" and card[1] == "1":
                card = card.replace("1", "", 1)
                card = card.replace("1", "J")
            elif card[0] == "1" and card[1] == "2":
                card = card.replace("1", "", 1)
                card = card.replace("2", "Q")
            elif card[0] == "1" and card[1] == "3":
                card = card.replace("1", "", 1)
                card = card.replace("3", "K")
        new_hand += card + " "
        valid_cards = new_hand.split()
    return valid_cards


def sort_and_tidy(hand):
    # Sorts the hand based on order of Rank list and tidies for output.
    t = []

    count_ranks = list(enumerate(ranks, 0))
    for values in count_ranks:
        for count, els in enumerate(hand):
            if els == values[1]:
                count = values[0]
                val = (count, els)
                t.append(val)
    get_values = [lis[1] for lis in t]
    output = re.sub("['\,\"\[\]]", "", str(get_values))
    return output


def print_invalid(hand):
    sys.stdout.write("Invalid: " + str(hand) + "\n")


def check_hand(hand):
    # Checks if hand can chunk and for valid cards, replaces 1,11,12,13 appropriately, sorts and prints.
    new_list = []
    vcount = 0
    if can_split(hand):
        chunks = re.split(r'/+|-+|\\s+', hand)
        tidy_chunks = re.sub("['\,\"\[\]]", "", str(chunks).upper())
        words = tidy_chunks.split(" ")
        new_list = replace(words)
        if valid_hand(new_list):
            sys.stdout.write(str(sort_and_tidy(new_list)) + "\n")
        else:
            print_invalid(hand)
    else:
        print_invalid(hand)



if __name__ == "__main__":
    input_hand = ""
    line = ""
    line = sys.stdin.readlines()
    for saved in line:
        check_hand(saved.rstrip())
