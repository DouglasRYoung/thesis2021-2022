import mysql.connector as mysql

# importing  all the
# functions defined in functions_.py
from data_pull_functions_ import *

all_cards_list = insert_all_cards()
print(all_cards_list)

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "thesis2021",
    database = "hearthstone"
)

print(db) # it will print a connection object if everything is fine

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()


##Drop Tables if manipulating stuff right now, we will use update later
#cursor.execute("DROP TABLE decks")
#cursor.execute("DROP TABLE cards")
cursor.execute("DROP TABLE allcards")

## creating a table called 'cards' in the 'hearthstone' database
## id: int . rest are varcharcard_name_api , card_cost , card_type , card_description, card_health , card_attack
cursor.execute("CREATE TABLE allcards (id INT(11) NOT NULL AUTO_INCREMENT PRIMARY KEY , card_name VARCHAR(255), card_cost VARCHAR(255), card_type VARCHAR(255), card_description VARCHAR(255), card_health  VARCHAR(255) , card_attack VARCHAR(255), card_rarity VARCHAR(255) , card_class VARCHAR(255) , many_classes VARCHAR(255))")
#cursor.execute("ALTER TABLE cards AUTO_INCREMENT=1")
#cursor.execute("INSERT INTO cards (id, card_name, card_cost , card_type , card_description, card_health , card_attack, card_rarity, card_class) VALUES ('0', 'example', '0' , 'SPELL', '', '1' , '1', 'COMMON', 'NEUTRAL') ")
#"INSERT INTO cards (id, card_name, card_cost , card_type , card_description, card_health , card_attack, card_rarity, card_class) VALUES(0, "example", "0" , "SPELL", "", "1" , "1", "COMMON", "NEUTRAL")"))

## defining the Query
query = "INSERT INTO allcards (card_name, card_cost , card_type , card_description, card_health , card_attack, card_rarity, card_class , many_classes) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

## executing the query with values
cursor.executemany(query, all_cards_list)

## to make final output we have to run the 'commit()' method of the database object
db.commit()


#################################
### Printing for confirmation ###
#################################

print(cursor.rowcount, "records inserted")

 ## defining the Query
query = "SELECT * FROM allcards"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)
