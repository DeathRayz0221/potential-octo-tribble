import random
import numpy as np
def shuffle(xs):
    size = len(xs)
    for jj in range(size):
        np.random.ran
        #newJ = random.randrange(0,size)      
        xs[jj],xs[newJ] = xs[newJ],xs[jj]
        
    
        
    return xs

deck = 4 * list("23456789TJQKA")
suits = 13 * list("CSDH")

suits.sort()
cards = [deck[jj] + suits[jj] for jj in range(len(deck))]

print(shuffle(cards))