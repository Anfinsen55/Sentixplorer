import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = open("text.txt", encoding='utf-8').read()

# encoding='utf-8' used for data that is imported from internet
lower_case = text.lower()

# removing special charecter

clean_text = lower_case.translate(str.maketrans("", "", string.punctuation))

# Tokenizing the sentence using nltk
tokenize_text = word_tokenize(clean_text, "english")

# print(tokenize_text)
# stop words using nltk


# reoving the stop words
final_word = []
for word in tokenize_text:
    if word not in stopwords.words('english'):
        final_word.append(word)
# print(final_word)

emotion_list = []
# Finding the emotion from the sentence
with open("emotions.txt", 'r') as file:
    for line in file:
        # removing the extraline and ','
        clear_line = line.replace("\n", "").replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_word:
            emotion_list.append(emotion)

print(emotion_list)

count = Counter(emotion_list)
print(count)


def sectimen_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score['neg']
    poss = score['pos']
    if neg > poss:
        print("Negative person")
    else:
        print("Possitive person")


sectimen_analyse(clean_text)

y = count.values()
z = count.keys()
plt.pie(y, labels=z)
plt.show()
"""
fig, axl = plt.subplots()
axl.bar(count.keys(), count.values())
fig.autofmt_xdate()
plt.savefig("Graph.png")
plt.show()

"""
