from collections import Counter

lines = [x for x in open('Day_7.txt').read().strip().split('\n')]
linepairs = [line.split(' ') for line in lines]

r = r2 = 0

# Heirarchy of hands, 5 of a kind is the best
heirarchy = {'high': 0, 'pair': 1, 'tp': 2, 'three': 3, 'fh': 4, 'four': 5, 'five': 6}

# Evaluate an array of hands, joker is a boolean for if we are using the part 2 rules
def evaluate(linepairs, joker):
    
    # The sorted array we will return
    sortedpairs = []
    

    if joker:
        # Part 2
        labels = 'AKQT98765432J'
    else:
        # Part 1
        labels = 'AKQJT98765432'

    # Iterate through all of the hands
    for index, linepair in enumerate(linepairs, start=0):

        # Parse the information
        cards = linepair[0]
        bid = linepair[1]
        type = ''
        
        # Counter object used to determine what kind of hand
        cardcounts = Counter(cards)
        
        # If we play by the Joker rules
        if joker:

            # If the most frequent card is a Joker, and there are 5 of them
            if cardcounts.most_common(1)[0][0] == 'J' and cardcounts.most_common(1)[0][1] == 5:
                # 'JJJJJ', thats a funny edge case.
                counts = (5,)
                
            # Any other case: <5 jokers
            else:
            
                # If we find any jokers, remove in the cardcounts just remove them
                if 'J' in cardcounts:
                    del cardcounts['J']
                    
                # Replace all instances of a Joker with the most common card. It doesn't matter which one this is.
                jokerhand = cards.replace('J', cardcounts.most_common(1)[0][0])
                
                # Now re count the hand.
                cardcounts = Counter(jokerhand)
                
                # Funky way of re arranging.
                counts = list(cardcounts.values())
                counts.sort(reverse=True)
                counts = tuple(counts)
                
        # If we aren't playing part 2 joker rules, this becomes quite easy.
        else:
            counts = list(cardcounts.values())
            counts.sort(reverse=True)
            counts = tuple(counts)
        
        # type tracks what pattern we have in the hand using the tuple we generated above.
        type = ''
        
        if counts == (1,1,1,1,1):
            type = 'high'
        elif counts == (2,1,1,1):
            type = 'pair'
        elif counts == (2,2,1):
            type = 'tp'
        elif counts == (3,2):
            type = 'fh'
        elif counts == (3,1,1):
            type = 'three'
        elif counts == (4,1):
            type = 'four'
        elif counts == (5,):
            type = 'five'
        else:
            pass
        
        # For the first hand, we just place it straight in.
        if(len(sortedpairs)) == 0:
            sortedpairs.append((cards, type, bid))
            continue

        # Search through the hands we have already sorted.
        for index, card in enumerate(sortedpairs, start = 1):
            
            # Get the type
            thistype = card[1]
            
            # placeholder to determine where we need to place this hand
            state = ''
            
            # We use the heirarchy dicitonary from above to figure out whether a hand is stronger or weaker.
            if heirarchy[type] < heirarchy[thistype]:
                state = 'lower'
            
            # If they are the same type, we need to look from left to right in the hand until we get a stronger card.
            elif heirarchy[type] == heirarchy[thistype]:
                for c in range(0,5):
                    
                    # Grab the current card
                    arraycard = card[0][c]
                    currentcard = cards[c]
                    
                    # Search for the index in the labels string, a lower index is stronger
                    if labels.find(arraycard) > labels.find(currentcard):
                        state = 'higher'
                        break
                    
                    
                    elif labels.find(arraycard) < labels.find(currentcard):
                        state = 'lower'
                        break
                    
                    # We are guaranteed that the hands are all different so there is no chance to handle two equal hands.
            
            # Case where the heirarchy is higher.
            elif heirarchy[type] > heirarchy[thistype]:
                state = 'higher'

            # If the hand is lower than sorted one, place it below.
            if state == 'lower':
                sortedpairs.insert(index-1, (cards, type, bid))
                break
                
            # If the hand is higher than the sorted one
            elif state == 'higher':
                
                # If we are at the end of the array we insert it.
                if index == len(sortedpairs):
                    sortedpairs.append((cards, type, bid))
                    break
                
                # If we are not at the end, we need to compare it to the next card.
                else:
                    continue
    
    # Return the full array of sorted pairs.
    return sortedpairs

p1arr = evaluate(linepairs, False)
p2arr = evaluate(linepairs, True)

# Perform the product and summing operation as required in the problem statement.
for i in range(0,len(p1arr)):
    r += (i+1) * int(p1arr[i][2])
    r2 += (i+1) * int(p2arr[i][2])
    
print(r)
print(r2)