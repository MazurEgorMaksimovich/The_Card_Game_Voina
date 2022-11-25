import random

class Card:
    """Одна игральная карта."""

    RANKS = ["Т", "2", "3", "4", "5", "6", "7", "8", "9", "10", "В", "Д", "К"]
    SUITS = [u'\u2660', u'\u2663', u'\u2665', u'\u2666']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    
    def __str__(self):
        ant = self.rank + self.suit
        return ant

class Unprintable_Card(Card):
    """Карта, номинал и масть которой не могут быть выведены на экран."""

    def __str__(self):
        return "<нельзя напечатать>"

class Positionable_Card(Card):
    """Карта, которую можно положить лицом или рубашкой вверх."""

    def __init__(self, rank, suit, face_up = True):
        super().__init__(rank, suit)
        self.is_face_up = face_up
    
    def __str__(self):
        if self.is_face_up:
            ant = super().__str__()
        else:
            ant = "XX"
        return ant
    
    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand:
    """Набор карт на руках у одного игрока."""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            ant = ""
            for card in self.cards:
                ant += str(card) + "\t"
        else:
            ant = "<пусто>"
        return ant
    
    def clear(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)
    
    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    """Колода игральных карт."""

    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать: карты закончились!")

players = int(input('Введите количество игроков: '))
hands = []
for player in range(players):
    hands.append(Hand())
play_deck = Deck()
play_deck.populate()
play_deck.shuffle()
play_deck.deal(hands)

the_great_stsch = [0]*players
choice = None
while choice != "0":
    print \
        ("""
        0 - Выйти
        1 - Играть
        """)
    
    choice = input("Ваш выбор: ")
    print()
    
    if choice == "1":
        the_stsch = 0
        the_biggest = 0
        for one_hand in hands:
            the_stsch += 1
            print(one_hand)
            card_nom = one_hand.__str__()[0:-2]
            try:
                int(card_nom)
                card_nom = int(card_nom)
            except ValueError:
                if card_nom == 'В':
                    card_nom = 11
                if card_nom == 'Д':
                    card_nom = 12
                if card_nom == 'К':
                    card_nom = 13
                if card_nom == 'Т':
                    card_nom = 14
            if card_nom > the_biggest:
                the_biggest = card_nom
                winner = str(the_stsch)
        the_great_stsch[int(winner)-1] += 1
        print("Игрок №" + winner + " победил в этом раунде.")

        for one_hand in hands:
            one_hand.clear()
        play_deck.shuffle()
        play_deck.deal(hands)

great_winner = 0
for player in range(0, len(the_great_stsch)):
    if the_great_stsch[player] > great_winner:
        great_winner = player+1

print("Игрок №" + str(great_winner) + " одержал наибольшее количество побед.")