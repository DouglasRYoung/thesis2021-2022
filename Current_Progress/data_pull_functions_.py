import requests
import re

# Function that takes card list and filters everything
def filter_card_list():

    card_list = []


    data = requests.get( 'https://api.hearthstonejson.com/v1/91456/all/cards.collectible.json' ).json()

    for card in data:
        card_name_api = card['name']['enUS']
        card_name_api = card_name_api.lower()
        card_name_api = card_name_api.replace('-' , '')
        card_name_api = card_name_api.replace('(' , '')
        card_name_api = card_name_api.replace(')' , '')
        card_name_api = card_name_api.replace(' ' , '')
        card_name_api = card_name_api.replace('1' , '')
        card_name_api = card_name_api.replace("'" , '')
        card_list.append((card_name_api , card))

    return card_list

# Function that takes the 30 cards of data and appends the deck win rate and deck type to then be put in MYSQL table
def merge_deck_data(card_list , win_rate_list , deck_type_list):
    i = 0
    all_lists = []
    while i < len(card_list):
        cards = card_list[i]
        win_rate_single = win_rate_list[i]
        win_rate_single = float(win_rate_single)
        print(win_rate_single)
        cards.append(win_rate_single)
        cards.append(deck_type_list[i])
        all_lists.append(cards)
        i += 1 
    return all_lists
# A Function that takes a list of card names and a list of the count per card name
# And returns a list of card names that equal 30
def make_full_deck(card_name , card_count):
    deck_list = []
    merged_list = [(card_name[i], card_count[i]) for i in range(0, len(card_name))]
    for x in merged_list:
        if (x[1] < 2):
            deck_list.append(x[0])
        else:
            deck_list.append(x[0])
            deck_list.append(x[0])
    return deck_list


#Get specific deck in list of decks by using Deck Num as # of deck that you return the information of
def get_deck(names, deck_types, win_ps , cards_lists , card_counts , deck_num):
    
    name = names[deck_num]
    deck_type = deck_types[deck_num]
    win_p = win_ps[deck_num]
    card_list = cards_lists[deck_num]
    card_count = card_counts[deck_num]

    return name, deck_type , win_p , card_list , card_count

# Function that removes duplicates in list 
def remove_dup(list_main):
    return_list = []
    for i in list_main:
        if i not in return_list:
            return_list.append(i)
            
    return return_list


# Retrieve Deck Data which includes : deck name , deck type , win percent of deck , cards , # of each card , 
def retrieve_data(filename):
    deck_name , class_type , deck_win_percentage = '' , '' , ''
    deck_name_list, class_type_list , win_percent_list , lil_array , lil_array1 = [] , [] , [] , [] , []
    big_array , big_array1  = [[]] , [[]]

    with open(filename,'r') as file: 


        # reading each line    
        for line in file:
            # reading each word       
            for words in line.split('href="/decks/'):
                #print(words)
                #Gets the deck name from url inspect
                if 'url(&quot;https://static.hsreplay.net/static/images/64x/class-icons' in words :
                    deck_name = words
                    deck_name = words.split(';);">',1)[1] 
                    deck_name = deck_name.split(';);">',1)[1]
                    deck_name = deck_name.split('</h3',1)[0]
                    deck_name_list.append(deck_name)
                #Gets the deck class from url inspect
                if 'data-card-class=' in words :
                    class_type = words 
                    class_type = words.split('data-card-class="' , 1)[1]
                    class_type = class_type.split('"' , 1)[0]
                    class_type_list.append(class_type)
                #Gets the deck win rate from url inspect
                if 'class="win-rate">' in words :
                    deck_win_percentage = words 
                    deck_win_percentage = words.split('"win-rate">' , 1)[1] 
                    deck_win_percentage = deck_win_percentage.split('<' , 1)[0] 
                    deck_win_percentage = deck_win_percentage.replace('%' , '')
                    win_percent_list.append(deck_win_percentage)
                if 'href="/c' in words:
                    lil_array = []
                    card_list_raw = words
                    #print(card_list_raw)
                    #card_list_raw = words.split('ards')
                    card_list_raw = words.split('class="card-icon"')
                    for i in card_list_raw:
                        if 'aria-label=' in i:
                            i = i.split('aria-label="' , 1)[1] 
                            i = i.replace('×' , '"')
                            i = i.replace('★' , '"')
                            i = i.split('"' , 1)[0] 
                            i = i.split("'" , 1)[0] 
                            i = i.split('1' , 1)[0] 
                            lil_array.append(i)
                    big_array.append(lil_array)

            for words in line.split('class="card-icon"'):
                #print(words)
                if 'aria-label="' in words :
                    words = words.split("style" , 1)[0] 
                    if '2' in words:
                        count = 2
                    else:
                        count = 1
                    lil_array1.append(count)
                if sum(lil_array1) == 30:
                    big_array1.append(lil_array1)
                    lil_array1 = [] 
    
        #Remove duplicates
        big_array = remove_dup(big_array)     
        del big_array1[0]
        del big_array[0]
        
        cards_list = big_array
        num_of_cards = big_array1
        return deck_name_list , class_type_list, win_percent_list, cards_list, num_of_cards

# Function that takes card's name and return information about card, will be used as function for all cards in deck
def get_card_info(card_name , list_Cards):
    

    card_cost = ''
    card_type = ''
    card_description = ''
    card_health = ''
    card_attack = ''
    card_rarity = ''
    card_class = ''
    many_classes = ''



    #data = requests.get( 'https://api.hearthstonejson.com/v1/91456/all/cards.collectible.json' ).json()

    for card in list_Cards:
        #print('card_1' , card[0])
        #print('card_2' , card_name)
        
        if card[0] == card_name:
            try:
                card_description = card[1]['text']['enUS']    
            except  KeyError as ke:
                card_description = ''

            try:
                card_cost =  card[1]['cost']  
            except  KeyError as ke:
                card_cost =  'none' 

            try:
                card_type = card[1]['type']     
            except  KeyError as ke:
                card_type = 'none'

            try:
                card_health = card[1]['health']      
            except KeyError as ke:
                card_health = ''

            try:
                card_attack = card[1]['attack']
            except KeyError as ke:
                card_attack = ''

            try:
                card_rarity = card[1]['rarity']  
            except  KeyError as ke:
                card_rarity = ''
            
            try:
                card_class = card[1]['cardClass']  
            except  KeyError as ke:
                card_class = ''

            try:
                many_classes = card[1]['classes'] 
                many_classes = many_classes[0]
                print(many_classes)
                #card_class = card[1]['cardClass'] 
            except  KeyError as ke:
                many_classes = ''

    return card_name , card_cost , card_type , card_description, card_health , card_attack, card_rarity, card_class, many_classes

#########################################################
### Following Functions for Pushing cards to Database ###
#########################################################

#Function will be used and takes in a list of decks: Function will return a list of card info for decks in list per deck
def push_card_data(deck_list , list_main):
    insert_list = []
    for card_list in deck_list:
        for card in card_list:
            card = card.lower()
            card = card.replace('-' , '')
            card = card.replace('(' , '')
            card = card.replace(')' , '')
            card = card.replace(' ' , '')
            card = card.replace('1' , '')
            card = card.replace("'" , '')

            card_name , card_cost , card_type , card_description, card_health , card_attack, card_rarity, card_class, many_classes = get_card_info(card , list_main)
            value_ = (card_name , card_cost , card_type , card_description, card_health , card_attack, card_rarity, card_class, many_classes)
            insert_list.append(value_)
    return insert_list

#Function will be used and takes in a list of decks: Function will return a list of card info for decks in list per deck
def push_card_data_new(card_list, list_main):
    insert_list = []
    for card in card_list:
            card = card.lower()
            card = card.replace('-' , '')
            card = card.replace('(' , '')
            card = card.replace(')' , '')
            card = card.replace(' ' , '')
            card = card.replace('1' , '')
            card = card.replace("'" , '')

            card_name , card_cost , card_type , card_description, card_health , card_attack, card_rarity, card_class, many_classes = get_card_info(card , list_main)
            value_ = (card_name , card_cost , card_type , card_description, card_health , card_attack, card_rarity, card_class, many_classes)
            insert_list.append(value_)
    return insert_list

def insert_all_cards():
    all_cards = filter_card_list()
    card_names = []
    for x in all_cards:
        card_names.append(x[0])
    card_values = push_card_data_new(card_names, all_cards)
    return card_values


