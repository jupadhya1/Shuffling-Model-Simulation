"""

# -*- coding: utf-8 -*-
"""TensorFlow with GPU

ID : JitendraUpadhyay10@gmail.com/a/45067900
Date: 12/09/2020 19:37:54
Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/notebooks/gpu.ipynb

# Tensorflow with GPU

This notebook provides an introduction to computing on a [GPU](https://cloud.google.com/gpu) in Colab. 
In this notebook you will connect to a GPU, and then run some basic TensorFlow operations on both the CPU and a GPU, 
observing the speedup provided by using the GPU.

## Enabling and testing the GPU

First, you'll need to enable GPUs for the notebook:

- Navigate to Edit→Notebook Settings
- select GPU from the Hardware Accelerator drop-down

Next, we'll confirm that we can connect to the GPU with tensorflow:
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf
device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  raise SystemError('GPU device not found')
print('Found GPU at: {}'.format(device_name))

"""## Observe TensorFlow speedup on GPU relative to CPU

This example constructs a typical convolutional neural network layer over a
random image and manually places the resulting ops on either the CPU or the GPU
to compare execution speed.
"""

# Commented out IPython magic to ensure Python compatibility.
# %tensorflow_version 2.x
import tensorflow as tf
import timeit

device_name = tf.test.gpu_device_name()
if device_name != '/device:GPU:0':
  print(
      '\n\nThis error most likely means that this notebook is not '
      'configured to use a GPU.  Change this in Notebook Settings via the '
      'command palette (cmd/ctrl-shift-P) or the Edit menu.\n\n')
  raise SystemError('GPU device not found')

def cpu():
  with tf.device('/cpu:0'):
    random_image_cpu = tf.random.normal((100, 100, 100, 3))
    net_cpu = tf.keras.layers.Conv2D(32, 7)(random_image_cpu)
    return tf.math.reduce_sum(net_cpu)

def gpu():
  with tf.device('/device:GPU:0'):
    random_image_gpu = tf.random.normal((100, 100, 100, 3))
    net_gpu = tf.keras.layers.Conv2D(32, 7)(random_image_gpu)
    return tf.math.reduce_sum(net_gpu)
  
# We run each op once to warm up; see: https://stackoverflow.com/a/45067900
cpu()
gpu()

# Run the op several times.
print('Time (s) to convolve 32x7x7x3 filter over random 100x100x100x3 images '
      '(batch x height x width x channel). Sum of ten runs.')
print('CPU (s):')
cpu_time = timeit.timeit('cpu()', number=10, setup="from __main__ import cpu")
print(cpu_time)
print('GPU (s):')
gpu_time = timeit.timeit('gpu()', number=10, setup="from __main__ import gpu")
print(gpu_time)
print('GPU speedup over CPU: {}x'.format(int(cpu_time/gpu_time)))
"""



# Program starts here
# Importing the necessary Libraries
import pandas as pd
import numpy as np
import sys
import time
import matplotlib.pyplot as plt
#%matplotlib inline
from random import randint

"""
    Function shuffle()
    ## input: sequence of integers DeckofCards that we want to shuffled, list or array
    ## output: sequence of shuffled integers deck_shuffled, np.array
"""
def shuffle(DeckofCards):
    ''' shuffle method
        Args:
            cards                            : list containg cards
        Returns:
            list of shuffled cards
     '''
    
    deck = np.array(DeckofCards)  
    n = len(deck) # Calculating the number of cards in the deck
    
    deck_shuffled = np.zeros(n) ## creating an placeholder for new deck for our shuffled cards
    n_right_original_cards = get_random_number_for_right_deck(n) 
    n_right = n_right_original_cards
    n_left = n - n_right_original_cards
    back = n-1
    for i in range(n):
        drop_right = should_drop_from_right_deck(n_left, n_right)
        print("n_left %s, n_right %s" %(n_left, n_right)) 
        
        if drop_right == True:
            print("RIGHT")
            print(back-i)
            deck_shuffled[back-i] = deck[n_right-1] ## the idea is to work from bottom of right deck
            n_right -= 1 # one less card in our right subdeck since it's on shuffled deck now
            print("\nCard that SHOULD be dropped: ", deck[n_right-1])
            print("Card dropped: ", deck_shuffled[back-i])
            
        else:
            print("LEFT")
            print(back-i)
            next_card = n_right_original_cards + n_left - 1 # index of next card to drop from left subdeck
            deck_shuffled[back-i] = deck[next_card]
            n_left -= 1 ## we now have one less card in our left subdeck
            print("\nCard that SHOULD be dropped: ", deck[next_card])
            print("Card dropped: ", deck_shuffled[back-i])
            
        
    return deck_shuffled

##
## functions used in shuffle to determine size of subdecks and from which subdeck to drop
##
    ## input: n total number of cards and the highest number that can be returned by this fn  
    ## output: int, how many cards should be split into the right subdeck
    
    ## when shuffling a real deck of cards, we split the deck roughly in half - want the same to happen here, so:
    ## should be (n, 0.5) whre n is the total number of cards

'''
Steps to perform:
Given a deck of n cards, at each round, do as follows.
Split the original deck into two decks according to the binomial distribution Bin(n,1/2).
Cut off the first k cards with probability (n k)2^n, put into the left deck, and put the rest n−k cards into the right deck.
Drop cards in sequence, where the next card comes from one of the two decks with probability proportional to the size of the deck at that time.
Suppose at a step there are L cards in the left deck and R cards in the right deck. A card is dropped from left with probability L/L+R, and from right otherwise.
'''

def get_random_number_for_right_deck(n): 
    ''' Generate random number for right deck
        Args:
            n : size of deck
        Returns:
            A random number between 0 and n including 0 and n
            Raise ValueError if n is negative or zero
        #For testing call
            get_random_number_for_right_deck(10)
    '''
    

    prob = 0.5 ## 'probability of success' - in Gilbert-Shannon-Reeds model should be 1/2
    
    num_right = np.random.binomial(n, prob)
    print(num_right)
    return num_right

'''
Should be
Based on probability of card actually coming from right deck: R / (R+L) 
where L and R are num cards in left and right deck respectively
so:
n_right / (n_left + n_right)
'''

    ## input: n_left, n_right ints - how many cards are in the left and right subdecks, respectively
    ## output: Boolean - tells us whether we should drop a card from the right subdeck (True) or left (False)
    

def should_drop_from_right_deck(n_left, n_right): 
    ''' Method for finding from which deck to drop
        Args:
            n_left : size of left deck
            n_right: size of right deck
        Return:
            Boolean value indicating it should drop from right deck or not
            Raise ValueError if n_left of n_right is negative
        #For testing call
            should_drop_from_right_deck(2,5)
    '''
    
    if (n_left > 0 and n_right > 0):
        
        prob = n_right / (n_right + n_left) ## probability that a card comes from right deck

        
        num = np.random.binomial(1, prob) ## bernoulli \equiv binomial with just a single trial
    
        print("\n n_right %s and n_left %s" %(n_right, n_left))
        print("prob is %s and num %s" %(prob, num))
        
        drop_right_bool = num == 1
        return drop_right_bool
    
    ## the rest is fine though
    elif (n_left == 0 and n_right > 0): ## left subdeck empty so we have to drop from the right deck
        ## print("\n n_right %s and n_left %s" %(n_right, n_left))
        return True
    
    elif (n_left > 0 and n_right == 0): ## right subdeck empty so we have to drop from the left deck
        ## print("\n n_right %s and n_left %s" %(n_right, n_left))
        return False 
    
    else: ## n_left and n_right = 0, empty subdecks
        ## print("\n n_right %s and n_left %s" %(n_right, n_left))
        raise ValueError("The subdecks are empty") ## can't drop from empty deck, n_right and/or n_left have to be >0

## now the decks we'll actually be considering:

DT26 = list(range(0, 26))
DT52 = list(range(0, 52))
DT104 = list(range(0, 104))

deck_list = np.array([DT26, DT52, DT104]) 
n = len(deck_list) 
num_shuffles = 7 

### so we can keep track of what the deck looks like after each indivisdual shuffle:

deck2_shuffles = np.zeros((num_shuffles+1, len(DT26)))
deck3_shuffles = np.zeros((num_shuffles+1, len(DT52)))
deck4_shuffles = np.zeros((num_shuffles+1, len(DT104)))


deck2_shuffles[0] = DT26
deck3_shuffles[0] = DT52
deck4_shuffles[0] = DT104

print("Let's consider where the original top and bottom cards of the unshuffled deck end up after 7 shuffles.")
print()

top_card_num_arr = np.zeros(n) ## keep track of our first to see where it ends up - in this case they're all 0
## but might have a case where it's not later, so.
bottom_card_num_arr = np.zeros(n) ## keep track of last element so we can see where it ends up

init_top_card_index = np.zeros(n) ## so we can compare later - all will remain zero since first index
init_bottom_card_index = np.zeros(n)

new_top_card_index = np.zeros(n) ## store the index of where the original top card ends up
new_bottom_card_index = np.zeros(n) ## '' '' bottom '' ''

## so we can keep our original decks if we need to use them later and bc otherwise Si won't be recognized

S2 = DT26
S3 = DT52
S4 = DT104

## shuffle each deck however many times we wanted to shuffle (declared above)
for i in range(num_shuffles):
    S2 = shuffle(S2)
    S3 = shuffle(S3)
    S4 = shuffle(S4)
    
    deck2_shuffles[i+1] = S2
    deck3_shuffles[i+1] = S3
    deck4_shuffles[i+1] = S4

## putting them in a list to make easier and shorter to access
shuffled_deck_list = [S2, S3, S4]

for i in range(n):
    ## store the first and last elements(top and bottom cards) of each deck
    top_card_num_arr[i] = deck_list[0][0]
    bottom_card_num_arr[i] = deck_list[i][-1]
    
    ## find indices of bottom card of deck (doing this way in case we change our deck sizes later)
    init_bottom_card_index[i] = len(deck_list[i]) - 1


    new_top_card_index[i] = np.where(shuffled_deck_list[i] == top_card_num_arr[i])[0][0]
    new_bottom_card_index[i] = np.where(shuffled_deck_list[i] == bottom_card_num_arr[i])[0][0]

    print("The shuffled deck %s is: \n %s \n" %(i+1, shuffled_deck_list[i]) )



