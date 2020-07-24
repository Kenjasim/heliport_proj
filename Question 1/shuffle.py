class Shuffle():
    """
    Class to perfectly shuffle a deck of cards
    """

    def __init__(self):
        """
        Creates a deck of cards
        """
        # Create the deck of cards using the cards class
        colours = ['heart', 'diamonds', 'spades', 'clubs']
        deck = [colour + ": " + str(value) for value in range(1, 14) for colour in colours]

        shuffle = self.perfect_shuffle(deck)
        print(shuffle)

    def perfect_shuffle(self, cards):
        """
        Splits the deck of cards in two and shuffles them

        Keyword Arguments
            cards - list of the deck of cards to shuffle

        Returns
            shuffled - list of the shuffled deck of cards
        """

        # Split into two halves
        firstHalf = cards[:len(cards)//2]
        secondHalf = cards[len(cards)//2:]

        # Declare the shuffled list
        shuffled = []

        # Loop through each list in paralell and append
        # to the shuffled list
        for f, s in zip(firstHalf, secondHalf):
            shuffled.append(f)
            shuffled.append(s)

        return shuffled

s = Shuffle()