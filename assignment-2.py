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
import pandas as pd # To work with dataframes and math functions
#import numpy as np # to work with math
import statsmodels.api as sm # To use OLS
import json # To work with json files
from textblob import TextBlob # To do Naïve Bayes classifification
from datetime import datetime # To format strings as dates
import textstat # To get fog gunning values
#from matplotlib.pylab import plt # To plot plots
#from sklearn.linear_model import LogisticRegression
#from sklearn.metrics import classification_report, confusion_matrix
import statsmodels.api as sm

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
pprint.pprint(
    ["Natural language processing is a concept where the automated generation and understanding of natural human languages are studied. The concept of readability is how a reader can understand a written text, moreover how hard or easy a text is to read. The readability measures depend on various “variables” i.e. Complexity of the words, the syntax, or the length of the sentences, depending on which model you are using. In the end, you get a value, which tells the reader how hard the text is to read. One way to measure, the readability measure is by the Fog index.",
              "When using the Fog index, the test aims to show the reader the difficulty level of the text. The level/index refers to the number of years of education a person needs to have to fully understand the text on the first reading.",
              "To calculate the Fog index, the following components must be known.",
              "    -    Average sentence length, percentage of long words and the sum of average sentence length and the percentage of long words.",
              "However, when checking for long words, there are some exceptions i.e. Company names, combines short-words and short three-syllable words.",
              "When writing in business language, you should aim for a score around 20-25, and in an office report a score of 30-35.",
              "NLP is used more than ever in financial research. Financial firms are using the NLP to parse textual data. Instead of having employees to check the textual data, the NLP are faster and more accurate than humans are. When using the NLP, companies are able to filter and analyze data faster. This allows companies to follow their stocks very closely and sell them if they discover that the company is budgeting with a loss in their earnings report.",
              "NLP can improve decision-making and speed inside financial organizations with three instances. Automation, Data enrichment, and Search and discovery."
      ]
)


#%% Excersice 2
# Forventningsafsnit
# mangler?

#%% Excersice 2 a
# Forventningsafsnit
pprint.pprint("Median and 50% quartile is effectivly the same. We asume that the exercise needs 75% quartile instead of a redundant median. This assumtion is for all of the assignment.")
pprint.pprint([
    "Mean:",
    "We would expect the mean to be around zero, as we would expect approximately the same amount of positive and negative words. However, given the type of data, and that people often are positive when it comes to new projects, one could argue that the mean probably is leaning to the positive side.",
    "Minimum and maximum:",
    "Initially we would expect the minimum value to be -1 and the maximum value to 1, however as seen in class, it is quite unusual to see a negative word valued -1, hence one might expect it to be a little larger.",
    "25%:",
    "We would expect the 25th quantile to be negative, as we would argue that there would be a minimum of 25% negative comments.",
    "50% / Median:",
    "As argued above, we would expect the median to be slightly above 0, as we would expect people to have a positive and open mind when it comes to new projects.",
    "75%:",
    "We would expect the 75th quantile to be around 0.3-0.5, as we would expect more positively weighted words, however we would argue that people rarely use words which are extremely positive, and hence weighted as 1. People are more likely to use less weighted positive words, even in extremely positive cases."
])

# Matematiske udregninger
pprint.pprint("Describe funktionen fra pandas anvendes til at retunere en oversigt der indeholder, antal, mean, standard deviation, min, 25%, median, 75% og max værdi for polarity index. Sd og 75% er ikke et krav, men anvnedt til analyse delen uanset.")

# Udregn polarity score
sentimetsPolarity = []
sentimetsSubjectivity = []
for review in icoDataFiltReview: # For every review in the filtered reviews
    tb = TextBlob(review) # Peform sentiment analasys
    sentimetsPolarity.append(tb.sentiment[0]) # Get polarity score
    sentimetsSubjectivity.append(tb.sentiment[1]) # Get subjectivity score

# Tilføj til dataframe
reviewDt["Polarity"] = sentimetsPolarity
reviewDt["Subjectivity"] = sentimetsSubjectivity

# Analyser tal
reviewDtSemanticInfo = reviewDt[['Polarity']].describe()
#median = reviewDt[['Polarity']].median()
#reviewDtSemanticInfo = reviewDtSemanticInfo.transpose()

pprint.pprint(reviewDtSemanticInfo)

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint([
    "Mean:",
    "We calculated a mean of 0.3, which shows that people tend to be more positive in the data. This is in compliance with what we discussed in the expectations, namely the fact that people tend to lean to the positive side when it comes to new projects.",
    "Minimum and maximum:",
    "We see a minimum of -0.7 and a maximum of 1. This is not in compliance with the initial thought, however it does fit what we have seen in class, with very few negative words actually being weighted as -1-",
    "25%:",
    "We see that the 25th quantile for the data is 0.1188, this is not what we expected. This deems to show that people tend to write fewer negative words than what we would expect. However, this is in compliance with what we mentioned above, with people tending to be more positive about startups.",
    "50% / Median:",
    "Same logic as with the 25th quantile. We expected the median to be slightly lower than the 0.2657 that we found. However, this might be reasoned by people being more positive about startups.",
    "75%:",
    "The 75th quantile is in compliance with what we initially thought. It is in the high end of what was expected, but nonetheless in compliance. This does make quite good sense, as people aren’t that likely to use very heavily weighted positive words, but instead opts for less heavily weighted words."
])


#%% Excersice 2 b
# Forventningsafsnit
pprint.pprint("We expect that the Fog index will be in the high end of the scale. This is because it is mostly university employees, professors, and people trading with crypto currencies that reads and comments on these projects.")

# Matematiske udregninger
pprint.pprint("Fog Index = 0.4 *(average # of words per sentence + 100 * percent of complex words)")


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
pprint.pprint([
    "The relevant results shows the opposite of what we expected. When calculating the Fog index, we see that the mean is around 12. From the results, we also see that the 50% quantile is lower than the mean. From this, we can see that reviews about the median are a lot higher than the median, which also visible when looking at max.",
    "However, when looking at the results it does make sense that the Fog index is low. This could be explained by the fact that the given text is short reviews. Reviews tend to be short and simple, making it easy to read."
    ])

#%% Excersice 2 c
# Forventningsafsnit
pprint.pprint("We expect that the overall rating will have a positive correlation between amount raised and the success of the project. However, we do not expect that the other variables correlate. The rating variables will most likely be more correlated than the other variables. ")

# Matematiske udregninger
pprint.pprint([
    "A correlation matrix measure of the linear association between two variables. It has a value between -1 and 1 where:",
    "•    -1 indicates a perfectly negative linear correlation between two variables",
    "•    0 indicates no linear correlation between two variables",
    "•    1 indicates a perfectly positive linear correlation between two variables",
    "The further away the correlation coefficient is from zero, the stronger the relationship between the two variables."
    ])
pprint.pprint("corr function from pandas is used on the datasetet to create a correlation matrix.")

# Udførelse af opgave
corrMatrix = reviewDt[['Polarity',
                       'Fog Index',
                       'Team rating',
                       'Vision rating',
                       'Product rating',
                       'Overall Rating',
                       'Amount Raised',
                       'Success']].corr()
                         # Missing from data: the team rating; the vision rating; the product rating; overall rating; amount raised; success (= dummy (1) if amount raised larger 0).
pprint.pprint(corrMatrix)

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint([
    "The correlation between Fog index, and everything but the amount raised is negative. This does intuitively make sense, as a high Fog index would make for more complicated reading, and hence you could assume that if the Fog index is high, less people would be able to actually use the text, and hence it would be rated lesser. However, people with a higher degree, might be able to invest more money, and hence it might make sense that there is a positive correlation here.",
    "Polarity generally has a positive correlation to the other variable, except fog index.",
    "Overall rating has a positive correlation to success. Then the overall rating increases, then there is a greater chance that the project will be successful."
    ])

#%% Excersice 2 d

# Matematiske udregninger
#pprint.pprint("") Mangler?

# Udførelse af opgave
#%% Excersice 2 d i
# Forventningsafsnit
pprint.pprint("Ordinary least square regression estimates the relationship between one or more independent variables and a dependent variable by minimizing the sum of the squares in the difference between the observed and the predicted values.")

# Run an OLS regression of the amount raised on polarity score,
# Fog index, the team rating, the vision rating, the product rating,
# overall rating. Interpret your results.

# OLS Regression
def ols_amountRaisedOn(X): # Give predictor value - does ols with amount raised as predictor - returns fitted ols estimate
    X = sm.add_constant(X) # add constant to predictor
    y = reviewDt[["Amount Raised"]] # response value
    est = sm.OLS(y, X) # Create model from response, y and predictor X
    est = est.fit() # fitting model
    #X_prime = np.linspace(X.iloc[:, 1].min(), X.iloc[:, 1].max(), 100)[:, np.newaxis]
    #X_prime = sm.add_constant(X_prime) 
    #y_hat = est.predict(X_prime)
    #fig = plt.xlabel("Amount Raised") 
    #fig = plt.ylabel(X.columns[1]) 
    #fig = plt.plot(X_prime[:, 1], y_hat, 'r', alpha=0.9)
    #plt.show()
    return est.summary() # return params

# > OLS:  Amount raised on polarity score, fog index, the team rating, the vision rating, the product rating, overall rating
olsResult = ols_amountRaisedOn(reviewDt[["Polarity", "Fog Index","Team rating", "Vision rating", "Product rating", "Overall Rating"]])
pprint.pprint(olsResult)

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("From the OLS regression we see that the Fog Index has a P-value of 0.000, hence we reject the impact of the Fog value on the amount raised. We see that the other variables are statistically significant on a 95% significance level for the amount raised. This does intuitively make sense, as Fog index only explains the difficulty of the text, and not wether it is positively or negatively weighted.")


# Logit regression
#%% Excersice 2 d ii
# Forventningsafsnit
pprint.pprint("Looking at the logit regression, we can reject everything but the be vision rating and the product rating on a 95% significance level.")

# 1 Import - done
# 2 Data - done
#reviewDt
# 3 Create model
#x = reviewDt[["Polarity"]]
x = reviewDt[["Polarity", "Fog Index","Team rating", "Vision rating", "Product rating", "Overall Rating"]]
y = reviewDt["Success"]
model = sm.Logit(y,x)
result=model.fit()
print(result.summary())
# 4 Evaluation

# Interpretation/Diskusion af øknomiske aspekter af resultatet
pprint.pprint("Hence, we see that vision rating and product rating seems to be the only relevant factors for success, however all but Fog index are relevant for the amount raised.")

#%% Excersice 2 outro
# Interpretation/Diskusion af øknomiske aspekter af resultatet
#pprint.pprint("") Mangler?


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
