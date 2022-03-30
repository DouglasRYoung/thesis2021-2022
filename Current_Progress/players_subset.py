import numpy as np
import warnings
from sklearn.metrics import SCORERS
from sqlalchemy import false, true
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)   
from Database_Connection import *
from regression import *
from Main_ import *
from NEW_data_pull import *

def card_Sets_playerspecific (card_db , card_list):
    Demon_Hunter_set, Druid_set, Hunter_set, Mage_set, Paladin_set, Priest_set, Rogue_set, Shaman_set, Warlock_set, Warrior_set = [],[],[],[],[],[],[],[],[],[]
    Demon_Hunter_set_check, Druid_set_check, Hunter_set_check, Mage_set_check, Paladin_set_check, Priest_set_check, Rogue_set_check, Shaman_set_check, Warlock_set_check, Warrior_set_check = [],[],[],[],[],[],[],[],[],[]
    for card in card_list:
        card_type = card_db["card_class"][card]
        card_name = card
        card_tag = card_db["card_name"][card]
        if ((card_type == "DEMONHUNTER") or (card_type == "NEUTRAL")):
            if card_tag not in Demon_Hunter_set_check:
                Demon_Hunter_set.append(card_name)
                Demon_Hunter_set_check.append(card_tag)
        if ((card_type == "DRUID") or (card_type == "NEUTRAL")):
            if card_tag not in Druid_set_check:
                Druid_set.append(card_name)
                Druid_set_check.append(card_tag)
        if ((card_type == "HUNTER") or (card_type == "NEUTRAL")):
            if card_tag not in Hunter_set_check:
                Hunter_set.append(card_name)
                Hunter_set_check.append(card_tag)
        if ((card_type == "MAGE") or (card_type == "NEUTRAL")):
            if card_tag not in Mage_set_check:
                Mage_set.append(card_name)
                Mage_set_check.append(card_tag)
        if ((card_type == "PALADIN") or (card_type == "NEUTRAL")):
            if card_tag not in Paladin_set_check:
                Paladin_set.append(card_name)
                Paladin_set_check.append(card_tag)
        if ((card_type == "PRIEST") or (card_type == "NEUTRAL")):
            if card_tag not in Priest_set_check:
                Priest_set.append(card_name)
                Priest_set_check.append(card_tag)
        if ((card_type == "ROGUE") or (card_type == "NEUTRAL")):
            if card_tag not in Rogue_set_check:
                Rogue_set.append(card_name)
                Rogue_set_check.append(card_tag)
        if ((card_type == "SHAMAN") or (card_type == "NEUTRAL")):
            if card_tag not in Shaman_set_check:
                Shaman_set.append(card_name)
                Shaman_set_check.append(card_tag)
        if ((card_type == "WARLOCK") or (card_type == "NEUTRAL")):
            if card_tag not in Warlock_set_check:
                Warlock_set.append(card_name)
                Warlock_set_check.append(card_tag)
        if ((card_type == "WARRIOR") or (card_type == "NEUTRAL")):
            if card_tag not in Warrior_set_check:
                Warrior_set.append(card_name)
                Warrior_set_check.append(card_tag)  

    #print("COUNT = " , count) 
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

###########################################################################################################################
def filter_card_names(card_set):
    refined_card_set = []
    for card_name_api in card_set:
        card_name_api = card_name_api.lower()
        card_name_api = card_name_api.replace('-' , '')
        card_name_api = card_name_api.replace("'" , '')
        card_name_api = card_name_api.replace('(' , '')
        card_name_api = card_name_api.replace(')' , '')
        card_name_api = card_name_api.replace(' ' , '')
        card_name_api = card_name_api.replace(',' , '')
        card_name_api = card_name_api.replace('1' , '')
        card_name_api = card_name_api.replace('2' , '')
        card_name_api = card_name_api.replace('3' , '')
        card_name_api = card_name_api.replace('4' , '')
        card_name_api = card_name_api.replace('5' , '')
        card_name_api = card_name_api.replace('6' , '')
        card_name_api = card_name_api.replace('7' , '')
        card_name_api = card_name_api.replace('8' , '')
        card_name_api = card_name_api.replace('9' , '')
        refined_card_set.append(card_name_api)

    return refined_card_set

def get_card_id(db , card_list):
    card_list_id = [] 
    for card in card_list:
        for index in db.index:
            card_name = db["card_name"][index]
            if card_name == card:
                card_list_id.append(db["card_id"][index])
                break
    card_list_id = [x-1 for x in card_list_id]
    return card_list_id


def main():
    card_set_1 = retrieve_new_data("MyCollection.txt")
    print(card_set_1)
    #card_set_filtered_1= filter_card_names(card_set_1)
    #card_set_1_id = get_card_id(dataframe_all , card_set_filtered_1)
    #player_class_sets = card_Sets_playerspecific(dataframe_all , card_set_1_id)
    #print(player_class_sets[0])


if __name__ == "__main__":
    main()