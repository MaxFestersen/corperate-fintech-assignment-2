# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 11:45:48 2021

@author: Max Festersen Hansen, Daniel Lindberg, Mads Duelund Dorka, Mathias Eriksen, Emilie Bruun Therp
"""

#%% Name and e-mail
print('Mads Duelund Dorka, mador17@student.sdu.dk')
print('Max Festersen Hansen, maxfh20@student.sdu.dk')
print('Mathias Eriksen, merik17@student.sdu.dk')
print('Daniel Lindberg, dlind16@student.sdu.dk')
print('Emilie Bruun Therp, emthe15@student.sdu.dk')

#%% Imports
import os
#import pandas as pd
import json # To work with json files
from textblob import TextBlob # To do Naïve Bayes classifification


#%% Enviroment and Data imports
os.chdir(os.path.dirname(os.path.realpath(__file__))) # Set dir
filename = 'icoData_19092018.json'

with open(filename) as json_data:
    icoData = json.load(json_data) #Load data into a list

icoData = [x for x in icoData if not len(x) == 1] # ???



#%% Excersice 1

#%% Excersice 2

#%% Excersice 2 a

#%% Excersice 2 b

#%% Excersice 2 c

#%% Excersice 2 d
#%% Excersice 2 d i

#%% Excersice 2 d ii

#%% Excersice 3

#%% Excersice 3 part 1

#%% Excersice 3 part 2

#%% Excersice 3 part 3
#%% Excersice 3 part 3 a

#%% Excersice 3 part 3 b

#%% Excersice 3 part 3 c

#%% Excersice 3 part 3 d
#%% Excersice 3 part 3 d i

#%% Excersice 3 part 3 d ii

