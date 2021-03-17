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
import os # To set dir
import pprint # To print "stuff" pretty
import pandas as pd
import json # To work with json files
from textblob import TextBlob # To do Naïve Bayes classifification
from datetime import datetime # To format strings as dates
import textstat # To get fog gunning values

#%% Enviroment and Data imports
os.chdir(os.path.dirname(os.path.realpath(__file__))) # Set dir
filename = 'icoData_19092018.json'

with open(filename) as json_data:
    icoData = json.load(json_data) #Load data into a list


#%% Formatting data
icoData = [x for x in icoData if not len(x) == 1]  # Filter list - remove empty dirs

icoDataFiltPersonNum = [] # For person instance
icoDataFiltReview = [] # For reviews
icoDataFiltReviewNum = [] # For a unique identifier for reviews
icoDataFiltTeamRating = [] # The team rating;
icoDataFiltVisionRating = [] # The vision rating;
icoDataFiltProductRating = [] # The product rating;
icoDataFiltOverallRating = [] # Overall rating;
icoDataFiltAmountRaised = [] # Amount raised;
icoDataFiltSuccess = [] # Successes

i = 0
personNum = 0
reviewNum = 0

# Loop all of icoData
for person in icoData:
    personNum += 1 # Count next person
    # Filter end-dates after 19-10-2018
    endDate = person['dates']["icoEnd"].split(" ")[0]
    if endDate != '0000-00-00' and datetime.strptime(endDate, "%Y-%m-%d") < datetime.strptime("2018-10-19", "%Y-%m-%d"):
        validDate = True # If the date is a valid date, and before 2018-10-19
    else:
        validDate = False
    if validDate:
        for rating in person['ratings']:
            if "review" in rating and len(rating["review"]) > 0:
                reviewNum += 1 # Count valid review
                # Save ratings review instance
                icoDataFiltPersonNum.append(personNum) # Person number for data validation
                icoDataFiltReviewNum.append(reviewNum) # Review number as uniqe classification
                icoDataFiltReview.append(rating['review']) # Review used in Exercise 2a-d and Exercise 3 part 1-3
                icoDataFiltTeamRating.append(rating["team"]) # Team rating from review
                icoDataFiltVisionRating.append(rating["vision"]) # Vision rating from review
                icoDataFiltProductRating.append(rating["product"]) # Product rating from review
                icoDataFiltOverallRating.append(person["rating"]) # Overall rating from person (NOTE: NOT REVIEW LEVEL)
                amountRaised = person["finance"]["raised"] # Amount raised
                icoDataFiltAmountRaised.append(amountRaised) # Append amount raised
                icoDataFiltSuccess.append(1 if amountRaised > 0 else 0) # Success (= dummy (1) if amount raised larger 0).
    i+=1 # Increment instance counter

# Format as dataframe
reviewDt = pd.DataFrame({   '#review': icoDataFiltReviewNum,
                            'Person ID': icoDataFiltPersonNum,
                            'Review':icoDataFiltReview,
                            'Team rating':icoDataFiltTeamRating,
                            'Vision rating':icoDataFiltVisionRating,
                            'Product rating':icoDataFiltProductRating,
                            'Overall Rating':icoDataFiltOverallRating,
                            'Amount Raised':icoDataFiltAmountRaised,
                            'Success':icoDataFiltSuccess
                         })

#%% Excersice 1
# Forventningsafsnit
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

#%% Excersice 2 a
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udregn polarity score
sentimetsPolarity = []
sentimetsSubjectivity = []
for review in icoDataFiltReview: # For every review in the filtered reviews
    tb = TextBlob(review) # Peform sentiment analasys
    sentimetsPolarity.append(tb.sentiment[0]) # Get polarity score
    sentimetsSubjectivity.append(tb.sentiment[0]) # Get subjectivity score

# Tilføj til dataframe
reviewDt["Polarity"] = sentimetsPolarity
reviewDt["Subjectivity"] = sentimetsSubjectivity

# Analyser tal
reviewDtSemanticInfo = reviewDt[['Polarity', 'Subjectivity']].describe()
#reviewDtInfo = reviewDtInfo.transpose()

pprint.pprint(reviewDtSemanticInfo)

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")


#%% Excersice 2 b
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Få Fog gunning værdier
fogValues = []
for review in icoDataFiltReview: # For every review in the filtered reviews
    fogValues.append(textstat.gunning_fog(review)) # Get and append fog index for review

# Tilføj til dataframe
reviewDt["Fog Index"] = fogValues

# Analyser tal
reviewDtFogInfo = reviewDt[['Fog Index']].describe()

pprint.pprint(reviewDtFogInfo)

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2 c
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave
corrMatrix = reviewDt[['Polarity', 'Fog Index']].corr()
# Missing from data: the team rating; the vision rating; the product rating; overall rating; amount raised; success (= dummy (1) if amount raised larger 0).

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2 d
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave
#%% Excersice 2 d i

#OLS regression
#%% Excersice 2 d ii

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 2 outro
# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")


#%% Excersice 3
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

#%% Excersice 3 part 1
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 2
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 3
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

#%% Excersice 3 part 3 a
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 3 b
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 3 c
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

# Udførelse af opgave

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 part 3 d
# Forventningsafsnit
pprint.pprint("")

# Matematiske udregninger
pprint.pprint("")

#%% Excersice 3 part 3 d i

#%% Excersice 3 part 3 d ii

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")


#%% Excersice 3 part 3 outro
# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")

#%% Excersice 3 outro
# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("")
