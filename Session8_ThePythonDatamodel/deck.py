class Deck:
    def __init__(self):
        self.cards = ['A', 'K', '4', '7']
    
    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return f'{self.cards}'

    def __setitem__(self, key, new_value):
        self.cards[key] = new_value

    def __delitem__(self, key):
        del(self.cards[key])

   



d = Deck()
# 1. kort --> __getitem__
print(d[1])

d[2] = 'BLA'

del(d[2])

print(d)


