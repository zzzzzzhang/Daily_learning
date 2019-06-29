
# coding: utf-8

# In[ ]:


import random


# In[ ]:


def poker(hands):
    """Return a list of winning hands: poker([hand,...]) => [hand,...]"""
    return max(hands, key=hand_rank)

def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    ranks = card_ranks(hand) 
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (2, two_pair(ranks), ranks)
    elif kind(2, ranks):
        return (1, kind(2, ranks), ranks)
    else:
        return (0, ranks)

def card_ranks(hand):
    """Return a list of the ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks


# In[ ]:


# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.

# teacher's
# def straight(ranks):
#     return (max(ranks) - min(ranks) == 4) and len(set(ranks)) == 5
    
def straight(ranks):
    list_straight = [ranks[0],ranks[0]-1,ranks[0]-2,ranks[0]-3,ranks[0]-4]
    return True if ranks == list_straight else False
        

def flush(hand):
    s = [s for r,s in hand]
    return len(set(s)) == 1
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    assert flush(sf) == True
    assert flush(fk) == False
    return 'tests pass'

print(test())


# In[ ]:


# Define a function, kind(n, ranks).
# teacher's
def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None

# def kind(n, ranks):
#     """Return the first rank that this hand has exactly n of.
#     Return None if there is no n-of-a-kind in the hand."""
#     counts = [ranks.count(r) for r in ranks]
#     if n not in counts:
#         return None
#     else:
#         return ranks[counts.index(n)]
    
def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "5S 5D 9H 9C 6S".split() # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

print(test())


# In[ ]:


# Define a function, two_pair(ranks).
#teacher's
# def two_pair(ranks):
#     """If there are two pair, return the two ranks as a
#     tuple: (highest, lowest); otherwise return None."""

#     pair = kind(2,ranks)
#     pair_low = kind(2,list(reversed(ranks)))
#     if (pair and pair_low != pair_low:
#         return (pair,pair_low)
#     else:
#         return None

def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    # Your code here.
    pair = kind(2,ranks)
    pair_low = kind(2,ranks[::-1])
    if (pair and pair_low) and pair != pair_low:
        return (pair,pair_low)
    else:
        return None

def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r 
    return None

def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    tp = "TD 9H TH 7C 3S".split() # Two Pair
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'
    
def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    return ranks

print(test())


# In[ ]:


# Modify the card_ranks(hand) function so that a 
# straight with a low ace (A, 2, 3, 4, 5) will be
# properly identified as a straight by the 
# straight() function.

# teacher's
# def card_ranks(hand):
#     "Return a list of the ranks, sorted with higher first."
#     ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
#     ranks.sort(reverse = True)
#     return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse = True)
    if ranks == [14,5,4,3,2]:
        ranks = [5,4,3,2,1]
    return ranks

def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5

def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split() # Straight Flush
    fk = "9D 9H 9S 9C 7D".split() # Four of a Kind
    fh = "TD TC TH 7C 7D".split() # Full House
    al = "AC 2D 4H 3D 5S".split() # Ace-Low Straight
    assert straight(card_ranks(al)) == True 
    return 'tests pass'

print(test())


# In[ ]:


def deal(numhands,n= 5,deck= [r+s for r in '23456789TJQKA' for s in 'SHDC']):
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]


# In[ ]:


deal(2)

