# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XLkjCHTAtK3HyYCUc7CGu4mMxebbm3i4
"""

import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
import nltk
nltk.download('movie_reviews')
nltk.download('stopwords')
nltk.download('punkt')
  
from nltk.corpus import movie_reviews
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def create_word_features(words):
    useful_words = [word for word in words if word not in stopwords.words("english")]
    my_dict = dict([(word, True) for word in useful_words])
    return my_dict

neg_reviews = []
for fileid in movie_reviews.fileids('neg'):
    words = movie_reviews.words(fileid)
    neg_reviews.append((create_word_features(words), "negative"))

pos_reviews = []
for fileid in movie_reviews.fileids('pos'):
    words = movie_reviews.words(fileid)
    pos_reviews.append((create_word_features(words), "positive"))

train_set = neg_reviews[:750] + pos_reviews[:750]
test_set =  neg_reviews[750:] + pos_reviews[750:]

classifier = NaiveBayesClassifier.train(train_set)
accuracy = nltk.classify.util.accuracy(classifier, test_set)
print(accuracy * 100)

classifier.show_most_informative_features(10)

review_spirit = '''
Spirited Away' is the first Miyazaki I have seen, but from this stupendous film 
I can tell he is a master storyteller. A hallmark of a good storyteller is making the audience 
empathise or pull them into the shoes of the central character. Miyazaki does this brilliantly in 
'Spirited Away'. During the first fifteen minutes we have no idea what is going on. 
Neither does the main character Chihiro. We discover the world as Chihiro does 
and it's truly amazing to watch. But Miyazaki doesn't seem to treat this world as something amazing. 
The world is filmed just like our workaday world would. 
The inhabitants of the world go about their daily business as usual as full with 
apathy as us normal folks. Places and buildings are not greeted by towering establishing shots 
and majestic music. 
The fact that this place is amazing doesn't seem to concern Miyazaki.
What do however, are the characters. Miyazaki lingers upon the characters as if they were actors.
He infixes his animated actors with such subtleties that I have never seen, even from animation 
giants Pixar. Twenty minutes into this film and I completely forgot these were animated characters; 
I started to care for them like they were living and breathing. 
Miyazaki treats the modest achievements of Chihiro with unashamed bombast. 
The uplifting scene where she cleanses the River God is accompanied by stirring music and is as exciting as watching gladiatorial combatants fight. Of course, by giving the audience developed characters to care about, the action and conflicts will always be more exciting, terrifying and uplifting than normal, generic action scenes. 
'''

words = word_tokenize(review_spirit)
words = create_word_features(words)
classifier.classify(words)

soty_rev = """The soulless characters makes film utterly boring for a sensible viewer.
Story is too shallow where a lot could have been explored in a college life.
Tiger is mocking audiences in the face, instead of being a stuntman he is being
projected as an actor just because of nepotism in Bollywood. """
words = word_tokenize(soty_rev)
words = create_word_features(words)
classifier.classify(words)