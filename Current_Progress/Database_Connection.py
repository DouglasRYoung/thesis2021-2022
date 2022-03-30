from cmath import nan
import mysql.connector as mysql
import numpy as np
import warnings
from pkg_resources import declare_namespace
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
#from hill_climbing_functions import *

                                        ##########################
                                        ### Database Beginning ###
                                        ##########################

## connecting to the database using 'connect()' method
## it takes 4 required parameters 'host', 'user', 'passwd', 'hearthsone'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "thesis2021",
    database = "hearthstone"
)

print(db) # it will print a connection object if everything is fine

## creating an instance of 'cursor' class which is used to execute the 'SQL' statements in 'Python'
cursor = db.cursor()

 ## defining the Query
query1 = "SELECT * FROM decks"

## getting records from the table
cursor.execute(query1)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

column_list = [ 'deck_id' , 'card1' , 'card2', 'card3' , 'card4', 'card5' , 'card6', 'card7' , 'card8', 'card9' , 'card10', 'card11' , 'card12', 'card13' , 'card14', 'card15' , 'card16', 'card17' , 'card18', 'card19' , 'card20','card21' , 'card22', 'card23' , 'card24', 'card25' , 'card26', 'card27' , 'card28', 'card29' , 'card30', 'win_rate' , 'deck_type']

dataframe_decks = pd.DataFrame(records)
dataframe_decks.columns = column_list
dataframe_decks = dataframe_decks.replace(r'^\s*$', np.nan, regex=True)

 ## defining the Query
query2 = "SELECT * FROM cards"

## getting records from the table
cursor.execute(query2)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

column_list = ['card_id' , 'card_name', 'card_cost' , 'card_type' , 'card_description', 'card_health' , 'card_attack', 'card_rarity', 'card_class', 'many_classes']
dataframe_cards = pd.DataFrame(records)
dataframe_cards.columns = column_list
dataframe_cards = dataframe_cards.replace(r'^\s*$', np.nan, regex=True)

 ## defining the Query
query3 = "SELECT * FROM allcards"

## getting records from the table
cursor.execute(query3)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

column_list = ['card_id' , 'card_name', 'card_cost' , 'card_type' , 'card_description', 'card_health' , 'card_attack', 'card_rarity', 'card_class' , 'many_classes']
dataframe_all = pd.DataFrame(records)
dataframe_all.columns = column_list
dataframe_all = dataframe_all.replace(r'^\s*$', np.nan, regex=True)

#list1 = dataframe_all["many_classes"]
#list1 = dataframe_cards["many_classes"].to_numpy()
#print(type(list1[0]) == float)
#print(np.isnan(list1[0]))
