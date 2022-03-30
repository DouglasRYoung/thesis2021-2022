from typing import final
import mysql.connector as mysql

# importing  all the
# functions defined in functions_.py
from data_pull_functions_ import *

#Similar to insert_Cards
filename = 'two_decks-text.txt'
deck_name_list , class_type_list , deck_win_percentage_list , card_names_lists , card_count_list= retrieve_data(filename)
#print(deck_name_list)
## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "thesis2021",
    database = "hearthstone"
)

##############
### Part 1 ###
##############

#Create 30 card deck using make_full_deck function from functions_.py
new_deck_list = [] 
i = 0
while i < len(card_names_lists):
    deck_x = make_full_deck(card_names_lists[i],card_count_list[i])
    #print('deck_x : ' , deck_x)
    new_deck_list.append(deck_x)
    i+=1

print('Number of decks' , len(new_deck_list))

##########################
### Database Beginning ###
##########################

print(db) # it will print a connection object if everything is fine

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

## Drop Table until Update
#cursor.execute("DROP TABLE decks")

## creating a table called 'cards' in the 'hearthstone' database
## card_name_api , card_cost , card_type , card_description, card_health , card_attack
cursor.execute("CREATE TABLE decks (id_deck INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY , card1 INT(11), FOREIGN KEY(card1) REFERENCES cards(id) , card2 INT(11), FOREIGN KEY(card2) REFERENCES cards(id), card3 INT(11), FOREIGN KEY(card3) REFERENCES cards(id), card4 INT(11), FOREIGN KEY(card4) REFERENCES cards(id), card5 INT(11), FOREIGN KEY(card5) REFERENCES cards(id), card6 INT(11), FOREIGN KEY(card6) REFERENCES cards(id), card7 INT(11), FOREIGN KEY(card7) REFERENCES cards(id), card8 INT(11), FOREIGN KEY(card8) REFERENCES cards(id), card9 INT(11), FOREIGN KEY(card9) REFERENCES cards(id), card10 INT(11), FOREIGN KEY(card10) REFERENCES cards(id), card11 INT(11), FOREIGN KEY(card11) REFERENCES cards(id), card12 INT(11), FOREIGN KEY(card12) REFERENCES cards(id), card13 INT(11), FOREIGN KEY(card13) REFERENCES cards(id), card14 INT(11), FOREIGN KEY(card14) REFERENCES cards(id), card15 INT(11), FOREIGN KEY(card15) REFERENCES cards(id), card16 INT(11), FOREIGN KEY(card16) REFERENCES cards(id), card17 INT(11), FOREIGN KEY(card17) REFERENCES cards(id), card18 INT(11), FOREIGN KEY(card18) REFERENCES cards(id), card19 INT(11), FOREIGN KEY(card19) REFERENCES cards(id), card20 INT(11), FOREIGN KEY(card20) REFERENCES cards(id), card21 INT(11), FOREIGN KEY(card21) REFERENCES cards(id), card22 INT(11), FOREIGN KEY(card22) REFERENCES cards(id), card23 INT(11), FOREIGN KEY(card23) REFERENCES cards(id), card24 INT(11), FOREIGN KEY(card24) REFERENCES cards(id), card25 INT(11), FOREIGN KEY(card25) REFERENCES cards(id), card26 INT(11), FOREIGN KEY(card26) REFERENCES cards(id), card27 INT(11), FOREIGN KEY(card27) REFERENCES cards(id), card28 INT(11), FOREIGN KEY(card28) REFERENCES cards(id), card29 INT(11) , FOREIGN KEY(card29) REFERENCES cards(id), card30 INT(11), FOREIGN KEY(card30) REFERENCES cards(id) , win_rate FLOAT(4), deck_type VARCHAR(255))")

#################################
### Pulling Values For Insert ###
#################################

# This should use select to make list of lists where inner lists are ints which are
# The foreign key of deck cards which is primary key of Cards table
big_list = []
bigger_list = []
for deck_a in new_deck_list:
    for card_a in deck_a:
        card_a = card_a.lower()
        card_a = card_a.replace('-' , ' ')
        card_a = card_a.replace('(' , '')
        card_a = card_a.replace(')' , '')
        card_a = card_a.replace(' ' , '')
        cursor.execute("SELECT id FROM cards WHERE card_name=%s " , (card_a,))
        record = cursor.fetchall()
        big_list.append(record)
    bigger_list.append(big_list)
    big_list = []
final_list = []
for list_x in bigger_list:
    print(list_x)
    id_key_list = [x[0] for x in list_x]
    id_key_list = [x[0] for x in id_key_list]
    final_list.append(id_key_list)
print('final_list_1: ' , final_list)
final_list = merge_deck_data(final_list , deck_win_percentage_list , class_type_list)
print('final_list_2: ' , final_list)

## Insert the list of lists of primary/foreign keys 
q1 = "INSERT INTO decks (card1 , card2 , card3 , card4 , card5 , card6 , card7 , card8 , card9 , card10 , card11 , card12 , card13 , card14 , card15 , card16 , card17 , card18 , card19 , card20 , card21 , card22 , card23 , card24 , card25 , card26 , card27 , card28 , card29 , card30 , win_rate, deck_type) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s, %s)" 
cursor.executemany(q1, final_list)

## to make final output we have to run the 'commit()' method of the database object
db.commit()

#################################
### Printing for confirmation ###
#################################

print(cursor.rowcount, "record inserted")

 ## defining the Query
query = "SELECT * FROM decks"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
#for record in records:
#    print(type(record))
#    for rec in record:
#        print(type(rec))
#    print(type(records))