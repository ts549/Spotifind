import string
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import matplotlib.pyplot as plt

def emotion_analysis(str): 
    """
    counts emotions in a given string using nltk

    :param str: string that you want to analyze
    :return map: map of emotions and counts 
    ex. Counter({' happy': 1, ' sad': 3})
    """
    lower_case = str.lower()
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

    # TOKENIZATION AND STOP WORDS
    tokenized_words = word_tokenize(cleaned_text, "english")

    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words.append(word)


    # EMOTIONS AND TEXT ANALYSIS
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
    return w

def sentiment_analysis(str):
    """
    measures sentiment in a given string using nltk 

    :param sentiment_text: text to analyze
    :return map: map of sentiments and values 
        ex. {'neg': 0.0, 'neu': 0.515, 'pos': 0.485, 'compound': 0.82}
    """
    lower_case = str.lower()
    cleaned_text = lower_case.translate(str.maketrans('','',string.punctuation))

    # TOKENIZATION AND STOP WORDS
    tokenized_words = word_tokenize(cleaned_text, "english")

    final_words = []
    for word in tokenized_words:
        if word not in stopwords.words('english'):
            final_words.append(word)


    # EMOTIONS AND TEXT ANALYSIS
    emotion_list = []
    with open('emotions.txt', 'r') as file:
        for line in file:
            clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')

            if word in final_words:
                emotion_list.append(emotion)

    w = Counter(emotion_list)
 
    score = SentimentIntensityAnalyzer().polarity_scores(str)
    print(score)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

    return score

def graph(w):
    """
    graphs emotions and stores in graph.png 

    :param w: array of counts of emotions
    """
    fig, ax1 = plt.subplots()
    ax1.bar(w.keys(), w.values())
    fig.autofmt_xdate()
    plt.savefig('graph.png')
    print("graph created successfully. check graph.png")
    plt.show()
    


textToProcess = "Hello My name is Sophia! I am really happy today :)"

print("\nEMOTION ANALYSIS")
w = emotion_analysis(textToProcess)

print("\nSENTIMENT ANALYSIS")
sentiment_analysis(textToProcess)

print("\nGRAPH")
graph(w)

