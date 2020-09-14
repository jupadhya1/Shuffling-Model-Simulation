"""# Part 2: Second Approach : 
Gilbert-Shannon-Reeds-Shuffling-Algorithm
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline

def get_random_number_for_right_deck(num):
    if num>0:
        return np.random.randint(0,num+1)
    else:
        raise ValueError("deck size cannot be less than or equal to zero")

def should_drop_from_right_deck(n_left, n_right):
    if n_left >= 0 and n_right >= 0:
        if n_right==0:
            return False
        elif n_left==0:
            return True
        else:
            randint=np.random.randint(1,n_left+n_right)
            return randint%2==0
    else:
        raise ValueError("n_left or n_right cannot be negative")

def shuffle(cards,get_random_number_for_right_deck,should_drop_from_right_deck):
    num=len(cards)
    n_right=get_random_number_for_right_deck(num)
    n_left=num-n_right
    leftIndex=-(num)
    shuffledCards=[]
    for i in range(num):
        if(should_drop_from_right_deck(n_left, n_right)):
            rightIndex=num-n_right
            shuffledCards.append(cards[rightIndex])
            n_right-=1
        elif n_left!=0:
            shuffledCards.append(cards[leftIndex])
            n_left-=1
            leftIndex+=1
    return np.array(shuffledCards)

#implenting Gibert shannon reeds model
def genrate_right_deck_gsr(num):
    if num>0:
        return np.random.binomial(num,p=0.5)
    else:
        raise ValueError("deck size cannot be less than or equal to zero")    
    
def drop_right_deck_gsr(n_left,n_right):

    if n_left >= 0 and n_right >= 0:
        if n_right==0:
            return False
        elif n_left==0:
            return True
        else:
            randint=np.random.binomial(num=1,p=n_right/(n_left+n_right))
            return randint==0
    else:
        raise ValueError("n_left or n_right cannot be negative")


#For testing GSR Shuffle call
#GSRShuffledCards=shuffle(cards,genrate_right_deck_gsr,drop_right_deck_gsr)

def differentiate_sequence(seq1,seq2):

    s1=set(seq1)
    s2=set(seq2)
    result=s1.intersection(s2)
    return len(result)

def caluclate_error_shuffle(seq1,seq2,div):

    l1=len(seq1)
    l2=len(seq2)
    caluclate_error_shuffle=0
    if l1== l2:
        if l1<=div:
            return np.square(l1)
        for i in range(l1):
            for j in range(l2):
                if i + div > l1:
                    break
                c1=sorted(seq1[i:i+div-1])
                if j+div >l2:
                    break
                c2=sorted(seq2[j:j+div-1])
                caluclate_error_shuffle+=np.square(differentiate_sequence(c1,c2))
    else:
        raise ValueError("sizes of sequences cannot be different")
    return caluclate_error_shuffle

def findRandomness(seq1,seq2):

    division=5 # checking for five overlapping sequence, i.e it can be any 5! combination
    overlapping5Error=caluclate_error_shuffle(seq1,seq2,division)
    max5Error = caluclate_error_shuffle(seq1,seq1,5)
    return 1-overlapping5Error/max5Error

def caluclateRandomnessShuffles(cards,sizeShuffle):
    ''' Calling shuffle method using using Gilbert-Shannon-Reeds model for different shuffle size and 
        calculating randomness for each of the shuffle
        Args:
            cards: original deck
            sizeShuffle: int of how many shuffle you have to perform
        Returns:
            pair of (NoOfshuffle,randomNess) indicating what is randomNess Value for each of successive shuffles
        
    '''
    NoOfshuffle=[]
    randomNess=[]
    GSRShuffledCards=shuffle(cards,genrate_right_deck_gsr,drop_right_deck_gsr)
    for i in range(sizeShuffle):
        r=findRandomness(cards,GSRShuffledCards)
        NoOfshuffle.append(i)
        randomNess.append(r)
        GSRShuffledCards=shuffle(GSRShuffledCards,genrate_right_deck_gsr,drop_right_deck_gsr)
    return NoOfshuffle,randomNess

def createGraph(NoOfshuffle,randdomNess,title,estimateShuffle):
    sizeShuffle=len(NoOfshuffle)
    y_intrsct = [estimateShuffle -2, estimateShuffle -1, estimateShuffle,estimateShuffle +1,estimateShuffle+2]
    x_intrsct = np.interp(y_intrsct, NoOfshuffle, randdomNess)

    fig, ax = plt.subplots(figsize=(10,10))
    ax.plot(randdomNess,NoOfshuffle, color='r')
    ax.set_xlabel(xlabel='RandomNess', size=20)
    ax.set_ylabel(ylabel='NoOfShuffles', size=20) 
    ax.set_title(title)
    custom_ticks=np.arange(1,sizeShuffle+1)
    ax.set_yticks(custom_ticks)

    ax.grid(axis='y')
    ax.vlines(x_intrsct, *ax.get_ylim())
    
    plt.show()

def boundaryCheckGSRalgo(startDeckSize,totalDecks,sizeShuffle):
    ''' implemets Gilbert-Shannon-Reeds model and plots graph for checking its implenting for 
        finding optimal no. of shuffles
        Args:
            startDeckSize: size of staring deck
            totalDecks   : it is no. of time startDeckSize muliply by 2 , i.e 26,52,104,208, so num here is 1,2,3,4
            sizeShuffle  : number fo shuffles to perform
        
    '''
    decks=[]
    a=startDeckSize
    for i in range(totalDecks):
        decks.append(a)
        a*=2

    for i in range(len(decks)):
        cards=np.arange(1,decks[i]+1)
        NoOfshuffle,randdomNess = caluclateRandomnessShuffles(cards,sizeShuffle)
        title='Deck of '+str(decks[i])
        estimateShuffle=np.floor(1.5*np.log2(decks[i]))
        createGraph(NoOfshuffle,randdomNess,title,estimateShuffle)

get_random_number_for_right_deck(10)

should_drop_from_right_deck(2,5)

cards=np.arange(1,53)
shuffle(cards,get_random_number_for_right_deck,should_drop_from_right_deck)

genrate_right_deck_gsr(10)

drop_right_deck_gsr(10)

caluclate_error_shuffle(cards,GSRShuffledCards,5)

#for checking
boundaryCheckGSRalgo(26,3,20)
