from matplotlib.cbook import ls_mapper
import requests
import re



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
            for words in line.split('href="/cards/'):
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



# Retrieve Deck Data which includes : deck name , deck type , win percent of deck , cards , # of each card , 
def retrieve_new_data(filename):
    #deck_name , class_type , deck_win_percentage = '' , '' , ''
    #deck_name_list, class_type_list , win_percent_list , lil_array , lil_array1 = [] , [] , [] , [] , []
    #big_array , big_array1  = [[]] , [[]]

    with open(filename,'r') as file: 
        card_name = ''
        card_name_list = []
        # reading each line    
        for line in file:
            # reading each word       
            for words in line.split('class="card-image" '):
                if 'href="/cards/' in words :
                    card_name = words
                    card_name = card_name.split('href="/cards/',1)[1] 
                    card_name = card_name.split('/',1)[1] 
                    card_name = card_name.split('"',1)[0] 
                    card_name_list.append(card_name)
                

        return 0

def main():
    p1_all_cards = retrieve_new_data("MyCollection.txt")

if __name__ == "__main__":
    main()

