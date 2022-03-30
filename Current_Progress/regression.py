import numpy as np
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning) 
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from Database_Connection import *

##############################
### Running Neural Network ###
##############################

#id_class = dataframe_decks[['deck_id']]
id_class = dataframe_decks.iloc[: , 1:31]
#print(id_class)
target_class = dataframe_decks[['win_rate']]
#print(target_class)


##########################
### Run Neural Network ###
##########################

X = id_class.to_numpy()
Y = target_class.to_numpy()

#X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.43, random_state=42)
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.43, random_state=2)

#neural =  LinearRegression().fit(X_train , Y_train)
#mlp = MLPRegressor(max_iter=3000 , activation='identity', solver = 'lbfgs')
mlp = MLPRegressor(max_iter=3000 , activation='identity', solver = 'lbfgs')
neural1 =  mlp.fit(X_train , Y_train)

#print('Deck Score: ' , Y_test)
#print('Predicted Score: ', neural1.predict(X_test))
