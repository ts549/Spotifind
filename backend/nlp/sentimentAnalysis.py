# CLEANING TEXT
# 1) create text file and take text from it
# 2) convert letters into lowercase
# 3) remove punctuations 

# utf encoding = way of writing text on the internet

import string
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import matplotlib.pyplot as plt

print("line 16")
text = open("read.txt", encoding='utf-8').read()
lower_case = text.lower()
# removes punctuations 1) letters to replace, 2) letters to replace letters to replace, 3) letters to delete
cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))
print(cleaned_text)

# TOKENIZATION AND STOP WORDS
# token => split sentence up, stop => words that don't do anything

# splitting text into words, word tokenize = faster than word.split
tokenized_words = word_tokenize(cleaned_text, "english")

# Removing stop words from the tokenized words list
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)


# EMOTIONS AND TEXT ANALYSIS
# compare words to emotions.txt
# remove extra lines, commas, and single quotes in emotions.txt, and strip to get rid of extra space
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

# NLTK Sentiment Analysis
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")


sentiment_analyse(cleaned_text)

# GRAPHING EMOTIONS USING MATPLOTLIB
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()