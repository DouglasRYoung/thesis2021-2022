import numpy as np
import warnings
from sklearn.metrics import SCORERS
from sqlalchemy import false, true
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
import random   
from Database_Connection import *
from neural_network import *
from main_functions_EDIT import *
###########################################################################################################################
def rem_duplicate(test_list):
    res = []
    for i in test_list: 
        if i not in res:
            res.append(i)
    return res

def has_tripicates(deck):
    res = []
    res1 = []
    for i in deck:
        if i not in res:
            res.append(i)
        else:
            if i not in res1:
                res1.append(i)
                res.append(i)
    return len(res) != len(deck)

def has_multiple_legendary(deck , database):
    legen_count = 0
    for i in deck:
        card_type = database["card_rarity"][i]
        if card_type == "LEGENDARY":
            legen_count += 1
        if legen_count > 1:
            return True
    return False

###########################################################################################################################

def deck_creation(deck_type_list):
    random_index = random.randint(0, 9)
    deck_type_cards = deck_type_list[random_index]
    created_deck = []
    deck_len = len(deck_type_cards)
    sample_list = random.sample(range(0, deck_len), 30)
    for ind in sample_list:
        created_deck.append(deck_type_cards[ind])
    #if has_multiple_legendary()
    #If condition to see if usable deck
    #If usable deck then return deck, Else: Re-do function
    return created_deck

def initial_deck_population(deck_type_list, number_of_decks):
    deck_list = []
    for num in range(0,number_of_decks):
        deck_x = deck_creation(deck_type_list)
        deck_list.append(deck_x)
    return deck_list

###########################################################################################################################

# Bubble sort to put scores in ascending order
def bubbleSort2(score):
    n = len(score)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if score[j] > score[j + 1] :
                score[j], score[j + 1] = score[j + 1], score[j]

# Function to utilize bubble sorted list and then go through zipped list of tuples (score, deck) 
# and create corresponding list of decks to the sorted list               
def getDeckOrder(score_refined , zipped_list):
    best_decks = []
    best_scores = []
    for i in score_refined:
        for (s,d) in zipped_list:            
            if (i == s):
                if type(d) is list:
                    d = d
                else:
                    d = d.tolist()
                if d not in best_decks:
                    best_decks.append(d)
                    best_scores.append(s)
                #print(d)
                #d = d.tolist()
    return best_decks , best_scores

#Scores the decks and sorts them in ascending order based on score
def GenerateScores(Decks, network):
    scores = network.predict(Decks)
    zipped_ = zip(scores , Decks)
    zipped_List = list(zipped_)
    bubbleSort2(scores)
    Decks , scores = getDeckOrder(scores , zipped_List)
    return Decks , scores

###########################################################################################################################
#
def Breed(Decks , db):
    i = 0
    score_list = []
    deck_list = []
    for i in range(len(Decks)):
        d1 = Decks[i]
        if i == ((len(Decks) - 1)):
            d2 = Decks[0] 
        else:
            d2 = Decks[i+1]
        d1 = d1[:15]
        d2 = d2[-15:]
        d1 = np.append(d1,d2)
        if has_tripicates(d1):
            score = -100
        if has_multiple_legendary(d1 , db):
            score = -100
        else:
            score = neural1.predict(d1.reshape(1, -1))
        score_list.append(score)
        deck_list.append(d1)
        i += 1
    Decks_breeded , scores = GenerateScores(deck_list, neural1)
    return Decks_breeded , scores 

def Mutation(Decks , db):
    number_of_mutations = random.randint(0,14)
    #print(number_of_mutations)
    Demon_Hunter_set, Druid_set, Hunter_set, Mage_set, Paladin_set, Priest_set, Rogue_set, Shaman_set, Warlock_set, Warrior_set = card_Sets(dataframe_cards)
    Type_List = [Demon_Hunter_set, Druid_set, Hunter_set, Mage_set, Paladin_set, Priest_set, Rogue_set, Shaman_set, Warlock_set, Warrior_set]
    for deck in Decks:
        #print("DECK AT BEGINNING" , deck)
        deck_type = deck_type_(deck , dataframe_cards)
        card_set = pick_card_set(deck_type)
        card_set = Type_List[card_set]
        for mutation_num in range(0 , number_of_mutations):
            random_index = random.randint(0, (len(card_set) - 1))
            new_card = card_set[random_index]
            ran_index2 = random.randint(0 , 29)
            deck_copy = deck
            deck_copy[ran_index2] = new_card
            if not has_tripicates(deck):
                if not has_multiple_legendary(deck , db):
                    deck[ran_index2] = new_card
    Decks_Mutated , Scores = GenerateScores(Decks , neural1)
    return Decks_Mutated , Scores

    
###########################################################################################################################

def One_Run_Function(initial_decks , card_Sets, network, database, breed_rate , mutation_rate , new_decks_percent, keep_deck_percent):
    if len(initial_decks) == 0:
        initial_decks = initial_deck_population(card_Sets , 100)

    Decks , Scores = GenerateScores(initial_decks , network)

    decks_length = len(Decks)

    Best_Decks = Decks[-keep_deck_percent:] , Scores[-keep_deck_percent:]
    Decks_To_Mutate = Decks[-breed_rate:] , Scores[-breed_rate:]
    Decks_To_Breed = Decks[-mutation_rate:] , Scores[-mutation_rate:]
    pop_new = initial_deck_population(card_Sets , new_decks_percent)

    Breeded_Decks , Breeded_Scores = Breed(Decks_To_Breed[0], database)
    Mutated_Decks , Mutated_Scores = Mutation(Decks_To_Mutate[0], database)

    new_deck_list = Best_Decks[0] + Breeded_Decks + Mutated_Decks + pop_new

    return new_deck_list

def main():
                                        ###################
                                        ### SPAWN DECKS ###
                                        ###################
    breed_rate = 70
    mutation_rate = 10
    new_decks_percent = 10
    keep_deck_percent = 10  

    card_sets = card_Sets(dataframe_cards)

    


if __name__ == "__main__":
    main()
















