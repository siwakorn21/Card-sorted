class Card :
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '(' + str(self.value) + ' ' + str(self.suit) + ')'

    def getScore(self):
        if self.value in '2345678910' :
            return int(self.value)
        elif self.value == 'A' :
            return 1
        else :
            return 10
    def comparevalue(self):
        if self.value in '345678910' :
            return int(self.value)
        elif self.value == 'A' :
            return 12
        elif self.value == '2' :
            return 13
        else :
            return 11
    def comparesuit(self):
        if self.suit == 'spade' : return 4
        elif self.suit == 'heart' : return 3
        elif self.suit == 'diamond' : return 2
        else : return 1
    def sum(self,other):
        return (Card(self.value,self.suit).getScore() + Card(other.value,other.suit).getScore())%10

    def __lt__(self,rhs):
        if Card(self.value,self.suit).comparevalue() != Card(rhs.value,rhs.suit).comparevalue() :
            return Card(self.value,self.suit).comparevalue() < Card(rhs.value,rhs.suit).comparevalue()

                
        else : return Card(self.value,self.suit).comparesuit() < Card(rhs.value,rhs.suit).comparesuit()


n = int(input())
cards = []
for i in range(n):
    value,suit = input().split()
    cards.append(Card(value,suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
    print(Card.sum(cards[i],cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
    print(cards[i])

