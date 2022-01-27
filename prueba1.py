import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import sentiment
from nltk import word_tokenize
nltk.download('vader_lexicon')
nltk.download('punkt')
analizador = SentimentIntensityAnalyzer()
print ('Dime algo')
sentences = input()
scores = analizador.polarity_scores(sentences)
print (scores)
        
#if (key,scores[key]) in range('1','0'):
#    (key,scores[key]) == True
#else:
#        (key,scores[key]) == False



if (scores['compound']) == 0:
    print ("Neutro")

elif (scores['compound']) < 0:
    print ('estoy mal')

else:
    print ('estoy bien')