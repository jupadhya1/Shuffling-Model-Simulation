# Shuffling-Model-Simulation
Gilbert-Shannon-Reeds model for shuffling.


## Installing

To install the dependencies, run:

```bash
pip install -r requirements.txt
```
---

## Run
Use --help to see tf_shuffle.py Usage.

```bash
  usage: tf_shuffle.py [-h] [DECK_SIZE] 

optional arguments:
  -h, --help            show this help message and exit
  --deck_size DECK_SIZE Add Deck size example 52
```

Riffle shuffle.

Example:
```bash
  python3 shuffle.py 52 
```
## Second Approach
python GSR_Algo_Second_Approach.py

## Test
boundaryCheckGSRalgo(26,3,20)

It will generate the output for first three sequence

---

## Test 
test for shuffle.py 
```bash
   python3 test_shuffle.py
```
---

## Plots

variation distance plot for deck size 26,56,104
File attached as Results.docx


## 
'''
Steps to perform:
Given a deck of n cards, at each round, do as follows.
Split the original deck into two decks according to the binomial distribution Bin(n,1/2).
Cut off the first k cards with probability (n k)2^n, put into the left deck, and put the rest n−k cards into the right deck.
Drop cards in sequence, where the next card comes from one of the two decks with probability proportional to the size of the deck at that time.
Suppose at a step there are L cards in the left deck and R cards in the right deck. A card is dropped from left with probability L/L+R, and from right otherwise.
'''
