from hashlib import new
import string
import numpy as np
import warnings
from scipy import rand
from sklearn.metrics import SCORERS
from sqlalchemy import false, true
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
import random   
from Database_Connection import *
from regression import *
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

def is_illegal_deck(deck , database):
    if has_multiple_legendary(deck, database):
        return True
    if has_tripicates(deck):
        return True
    return False

###########################################################################################################################

def card_Sets (card_db):
    Demon_Hunter_set, Druid_set, Hunter_set, Mage_set, Paladin_set, Priest_set, Rogue_set, Shaman_set, Warlock_set, Warrior_set = [],[],[],[],[],[],[],[],[],[]
    Demon_Hunter_set_check, Druid_set_check, Hunter_set_check, Mage_set_check, Paladin_set_check, Priest_set_check, Rogue_set_check, Shaman_set_check, Warlock_set_check, Warrior_set_check = [],[],[],[],[],[],[],[],[],[]
    for index in card_db.index:
        card_type = card_db["card_class"][index]
        card_id = index
        #card_db["card_id"][index]
        card_name = card_db["card_name"][index]
        card_multi = card_db["many_classes"][index]
        if ((card_type == "DEMONHUNTER") or (card_type == "NEUTRAL")):
            if card_multi == "DEMONHUNTER" or (type(card_multi) == float) :
                Demon_Hunter_set.append(card_id)
                Demon_Hunter_set_check.append(card_name)
        if ((card_type == "DRUID") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "DRUID":
                Druid_set.append(card_id)
                Druid_set_check.append(card_name)
        if ((card_type == "HUNTER") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "HUNTER":
                Hunter_set.append(card_id)
                Hunter_set_check.append(card_name)
        if ((card_type == "MAGE") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "MAGE":
                Mage_set.append(card_id)
                Mage_set_check.append(card_name)
        if ((card_type == "PALADIN") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "PALADIN":
                Paladin_set.append(card_id)
                Paladin_set_check.append(card_name)
        if ((card_type == "PRIEST") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "PRIEST":
                Priest_set.append(card_id)
                Priest_set_check.append(card_name)
        if ((card_type == "ROGUE") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "Rogue":
                Rogue_set.append(card_id)
                Rogue_set_check.append(card_name)
        if ((card_type == "SHAMAN") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "SHAMAN":
                Shaman_set.append(card_id)
                Shaman_set_check.append(card_name)
        if ((card_type == "WARLOCK") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "WARLOCK":
                Warlock_set.append(card_id)
                Warlock_set_check.append(card_name)
        if ((card_type == "WARRIOR") or (card_type == "NEUTRAL")):
            if (type(card_multi) == float) or card_multi == "WARRIOR":
                Warrior_set.append(card_id)
                Warrior_set_check.append(card_name)    
    Demon_Hunter_set = rem_duplicate(Demon_Hunter_set)
    Druid_set = rem_duplicate(Druid_set)
    Hunter_set = rem_duplicate(Hunter_set)
    Mage_set = rem_duplicate(Mage_set)
    Paladin_set = rem_duplicate(Paladin_set)
    Priest_set = rem_duplicate(Priest_set)
    Rogue_set = rem_duplicate(Rogue_set)
    Shaman_set = rem_duplicate(Shaman_set)
    Warlock_set = rem_duplicate(Warlock_set)
    Warrior_set = rem_duplicate( Warrior_set)
    return Demon_Hunter_set, Druid_set, Hunter_set, Mage_set, Paladin_set, Priest_set, Rogue_set, Shaman_set, Warlock_set, Warrior_set

def pick_card_set(deck_class):
    set = 0
    if (deck_class == "DEMONHUNTER"):
        set = 0
    if (deck_class == "DRUID"):
        set = 1
    if (deck_class == "HUNTER"):
        set = 2
    if (deck_class == "MAGE"):
        set = 3
    if (deck_class == "PALADIN"):
        set = 4
    if (deck_class == "PRIEST"):
        set = 5
    if (deck_class == "ROGUE"):
        set = 6
    if (deck_class == "SHAMAN"):
        set = 7
    if (deck_class == "WARLOCK"):
        set = 8
    if (deck_class == "WARRIOR"):
        set = 9 

    return set

def deck_type_(deck , card_db):
    deck_type = ""
    for card_id in deck:
        card_type = card_db["card_class"][card_id]
        card_multi = card_db["many_classes"][card_id]
        if (card_type == "DEMONHUNTER"):
            deck_type = card_type
            return deck_type
        if (card_type == "DRUID"):
            deck_type = card_type
            return deck_type
        if (card_type == "HUNTER"):
            deck_type = card_type
            return deck_type
        if (card_type == "MAGE"):
            deck_type = card_type
            return deck_type
        if (card_type == "PALADIN"):
            deck_type = card_type
            return deck_type
        if (card_type == "PRIEST"):
            deck_type = card_type
            return deck_type
        if (card_type == "ROGUE"):
            deck_type = card_type
            return deck_type
        if (card_type == "SHAMAN"):
            deck_type = card_type
            return deck_type
        if (card_type == "WARLOCK"):
            deck_type = card_type
            return deck_type
        if (card_type == "WARRIOR"):
            deck_type = card_type
            return deck_type  
        if type(card_multi) == string:
            deck_type = card_multi
            return deck_type
    return "NEUTRAL"

###########################################################################################################################

def deck_creation(class_type , Sets_Of_Cards , database):
    original_deck = []
    created_deck = []
    #List of cards of type
    deck_type_cards = Sets_Of_Cards[class_type]
    for ind in range(0,30):
        new_card = random.choice(deck_type_cards)
        created_deck.append(new_card)
        while is_illegal_deck(created_deck , database):
            del created_deck[-1]
            new_cards = random.choice(deck_type_cards)
            created_deck.append(new_cards)
            new_card = new_cards
        original_deck.append(new_card)
        
    return original_deck

    #deck_len = len(deck_type_cards)
    #sample_list = random.sample(range(0, deck_len), 30)
    #for ind in range(0,30):
     #   new_card = random.randint(0,deck_len)
      #  created_deck.append(new_card)
       # while is_illegal_deck(created_deck , database):
        #    created_deck = original_deck
         #   new_card = random.randint(0,deck_len)
          #  created_deck.append(new_card)
           # #print(is_illegal_deck(original_deck, database))
    #    original_deck.append(new_card)
    #    print(is_illegal_deck(original_deck, database))
    #    print(original_deck)
    #    ind += 1
    #return original_deck

def initial_deck_population(deck_type_list, number_of_decks, database):
    deck_list = []
    num = 0
    for num in range(0,number_of_decks):
        random_index = random.randint(0, 9)
        deck_x = deck_creation(random_index, deck_type_list , database)
        deck_list.append(deck_x)
        num += 1
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
    d1 = []
    d2 = []
    score_list = []
    deck_list = []
    for deck in Decks:
        d1 = deck
        d1_type = deck_type_(d1,db)
        for deck2 in Decks:
            d2 = deck2
            d2_type = deck_type_(d2,db)
            # change this to d1_type == d2_type and d1 != d2
            if d1_type == d2_type:
                #print(d1_type)
                #print(d2_type)
                #print("deck 1 for breed" ,d1)
                #print("deck 2 for breed" , d2)
                d1 = d1[:15]
                d2 = d2[-15:]
                d1 = np.append(d1,d2)
                if is_illegal_deck(d1, db):
                    score = -100
                else:
                    score = neural1.predict(d1.reshape(1, -1))
                score_list.append(score)
                deck_list.append(d1)
    Decks_breeded , scores = GenerateScores(deck_list, neural1)
    return Decks_breeded , scores 

def Mutation(Decks , db):
    #number_of_mutations = random.randint(0,14)
    #print(number_of_mutations)
    #is_illegal_deck(deck , database)
    Demon_Hunter_set, Druid_set, Hunter_set, Mage_set, Paladin_set, Priest_set, Rogue_set, Shaman_set, Warlock_set, Warrior_set = card_Sets(db)
    Type_List = [Demon_Hunter_set, Druid_set, Hunter_set, Mage_set, Paladin_set, Priest_set, Rogue_set, Shaman_set, Warlock_set, Warrior_set]
    for deck in Decks:
        #print("DECK AT BEGINNING" , deck)
        deck_type = deck_type_(deck , db)
        card_set = pick_card_set(deck_type)
        card_set = Type_List[card_set]
        for mutation_num in range(0 , 1):
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
        initial_decks = initial_deck_population(card_Sets, 100, database)

    Decks , Scores = GenerateScores(initial_decks , network)

    Best_Decks = Decks[-keep_deck_percent:] , Scores[-keep_deck_percent:]
    Decks_To_Breed = Decks[-breed_rate:] , Scores[-breed_rate:]
    Decks_To_Mutate = Decks[-mutation_rate:] , Scores[-mutation_rate:]
    pop_new = initial_deck_population(card_Sets , new_decks_percent, database)

    Breeded_Decks , Breeded_Scores = Breed(Decks_To_Breed[0], database)
    Mutated_Decks , Mutated_Scores = Mutation(Decks_To_Mutate[0], database)

    new_deck_list = Best_Decks[0] + Breeded_Decks + Mutated_Decks + pop_new

    return new_deck_list

def final_function(iterations , subset_cards , network , database, breed_rate , mutation_rate , new_decks_percent, keep_deck_percent):
    decks = []
    scores = []
    for iter in range(0, (iterations)):
        decks  = One_Run_Function(decks , subset_cards , network, database,  breed_rate , mutation_rate , new_decks_percent, keep_deck_percent)
        decks , scores = GenerateScores(decks , network)
    print(print_information(decks , scores, 300 , database))   
    return decks , scores

###########################################################################################################################

def print_information(decks , scores , iteration , database):
    print("Iteration: " , iteration)
    print("Worst Deck: " , id_to_names(decks[0] , database))  
    print("Worst Deck Score: " , scores[0])
    print("Worst Deck Type: " , deck_type_(decks[0] , database))
    print("Best Deck: " , id_to_names(decks[-1] , database))
    print("Best Deck Score: " , scores[-1])
    print("Best Deck Type: " , deck_type_(decks[-1] , database))
    return 0

def id_to_names(deck , card_db):
    deck_name_list = []
    for card in deck:
        deck_name_list.append(card_db["card_name"][card])

    return deck_name_list

###########################################################################################################################


def main():
                                        ###################
                                        ### SPAWN DECKS ###
                                        ###################
    breed_rate = 20
    mutation_rate = 50
    new_decks_percent = 20
    keep_deck_percent = 10  

    card_sets = card_Sets(dataframe_all)

    #init_decks = initial_deck_population(card_sets, 15, dataframe_all)

    #result = One_Run_Function([], card_sets, neural1, dataframe_all, breed_rate , mutation_rate , new_decks_percent, keep_deck_percent)

    #decks , scores = final_function(100, card_sets , neural1 , dataframe_all, breed_rate , mutation_rate , new_decks_percent, keep_deck_percent)
    #print(decks[-1])
    #print(scores[-1])s

    deck = [1716, 3620, 1536, 1019, 982, 169, 3288, 1781, 2267, 2921, 2807, 770, 188, 1381, 1545, 679, 693, 2633, 133, 3752, 1211, 97, 323, 739, 3070, 2063, 371, 1500, 1665, 373]
    deck = np.array(deck)
    print(neural1.predict(deck.reshape(1, -1)))
    #for x in deck:
    #   print(dataframe_all["card_cost"][x])
       

if __name__ == "__main__":
    main()



























