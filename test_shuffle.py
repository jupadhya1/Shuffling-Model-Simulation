import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py
from sys import argv
%matplotlib inline

from tf_shuffle import shuffle

def check_shuffle(deck):
    count = 0
    for i in range(len(deck)-2):
        diff = deck[i+1] - deck[i]
        if (abs(deck[i+2] - deck[i+1]) == diff) and (abs(deck[i+1] - deck[i]) == diff):
            count += 1
        else:
            count = count
    return count

def recurse(deck):
    count = 0
    for i in range(len(deck)-1):
        if deck[i] == deck[i+1]:
            count+=1
        else:
            count = count
    return count





D0 = np.array(range(0,0)) 
S0 = shuffle(D0) 
DT26 = list(range(0, 26))
DT52 = list(range(0, 52))
DT104 = list(range(0, 104))

deck_list = np.array([DT26, DT52, DT104]) 
n = len(deck_list)  

num_shuffles = 10 



shuffle_deck_2 = np.zeros((num_shuffles+1, len(DT26)))
shuffle_deck_3 = np.zeros((num_shuffles+1, len(DT52)))
shuffle_deck_4 = np.zeros((num_shuffles+1, len(DT104)))


shuffle_deck_2[0] = DT26
shuffle_deck_3[0] = DT52
shuffle_deck_4[0] = DT104

print("Let's consider where the original top and bottom cards of the unshuffled deck end up after %s shuffles." %(num_shuffles))
print()

top_card_num_arr = np.zeros(n) 

bottom_card_num_arr = np.zeros(n) 

init_top_card_index = np.zeros(n) 
init_bottom_card_index = np.zeros(n)

new_top_card_index = np.zeros(n) 
new_bottom_card_index = np.zeros(n) 


S2 = DT26
S3 = DT52
S4 = DT104


for i in range(1, num_shuffles):

    S2 = shuffle(S2).tolist()
    S3 = shuffle(S3).tolist()
    S4 = shuffle(S4).tolist()


    shuffle_deck_2[i] = S2
    shuffle_deck_3[i] = S3
    shuffle_deck_4[i] = S4


shuffled_deck_list = [S2, S3, S4]

for i in range(n):
    top_card_num_arr[i] = deck_list[0][0]
    bottom_card_num_arr[i] = deck_list[i][-1]

    init_bottom_card_index[i] = len(deck_list[i]) - 1

    new_top_card_index[i] = shuffled_deck_list[i].index(top_card_num_arr[i])
    new_bottom_card_index[i] = shuffled_deck_list[i].index(bottom_card_num_arr[i])
    print("The shuffled deck %s is: \n %s \n" %(i+1, shuffled_deck_list[i]) )

        
for i in range(len(deck_list)):
    print("%s cards: \n%s" %(len(deck_list[i]), shuffled_deck_list[i]))
    print()
    print("%s cards, initial index %s (top card) --> index %s" %(len(deck_list[i]), init_top_card_index[i], new_top_card_index[i]))
    print("Top card moved %s positions" %(new_top_card_index[i] - init_top_card_index[i]))
    print("%s cards, initial index %s (bottom card) --> index %s" %(len(deck_list[i]), init_bottom_card_index[i], new_bottom_card_index[i]))
    print("Bottom card moved %s positions" %(init_bottom_card_index[i] - new_bottom_card_index[i]))
    print()

       
###
#Test Cases
print("Let's look at whether there are still groups of consecutive cards.")
print("We'll consider a consecutive group to be 3 ordered cards in a row.")
print()

print("Let's compare consecutive shuffles of 26 cards:")
print()
grps = np.zeros(num_shuffles)
for row in range(num_shuffles):
    print("Shuffle %s: %s\n" %(row, shuffle_deck_2[row]))
    grps[row] = check_shuffle(shuffle_deck_2[row])
print("List of number of ordered sequences at each iteration: ", grps)
plt.plot(grps)
plt.show()

print("Let's compare consecutive shuffles of 52 cards:")
print()
grps = np.zeros(num_shuffles)
for row in range(num_shuffles):
    print("Shuffle %s: %s\n" %(row, shuffle_deck_3[row]))
    grps[row] = check_shuffle(shuffle_deck_3[row])
print("List of number of ordered sequences at each iteration: ", grps)
print("And we can see that at around 7 shuffles, we stop seeing two number groupings as much as well.")
plt.plot(grps)
plt.show()

print("Let's compare consecutive shuffles of 104 cards:")
print()
grps = np.zeros(num_shuffles)
for row in range(num_shuffles):
    ## print("Shuffle %s: %s\n" %(row, shuffle_deck_4[row]))
    grps[row] = check_shuffle(shuffle_deck_4[row])
print("List of number of ordered sequences at each iteration: ", grps)
plt.plot(grps)
plt.show()

