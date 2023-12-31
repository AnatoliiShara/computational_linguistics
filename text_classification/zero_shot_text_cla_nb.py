# -*- coding: utf-8 -*-
"""zero_shot_text_cla_nb.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15gG7h4VweD9A4N8_VHFm70ddu-menG5y
"""

from typing import List
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# define category labels
categories = ["Travel", "Sports", "Technology", "Politics", "Weather"]

# Define training data for each category
training_data = {
    "Travel": [
        "Ukraine, a country in Eastern Europe, has a rich cultural heritage and a diverse landscape."
    ],
    "Legislation": [
        "In the corridors of power, legislation takes shape through rigorous debate, research, and public discourse.",
        "Laws are the embodiment of a society's values, addressing contemporary challenges and envisioning a better future." ,
        "Legal frameworks evolve, adapting to the changing needs of communities and embracing principles of equality and justice."
    ],
    "Sports": [
        "Football, also known as soccer in some parts of the world, is a globally beloved sport with a massive following.",
        "In the world of football, every match is a saga of determination and teamwork."
        "Players, guided by coaches, strive for excellence on the field, showcasing their talent and dedication.",
        "From grassroots development to elite competitions, football fosters discipline, resilience, and the pursuit of dreams.",
        "Behind every goal and every victory lies hours of training, strategic planning, and unwavering passion, making football not just a sport but a way of life for enthusiasts around the globe.",
        "Football, the beautiful game, unites people from diverse backgrounds under the banner of passion and competition.",
        "Stadiums echo with the cheers of fans, celebrating the artistry of players and the thrill of goals.",
    ]
}

# preprocess training data

documents = []
labels = []
for category, docs in training_data.items():
  documents.extend(docs)
  labels.extend([category] * len(docs))

# instantiate a vectorizer to convert text into numerical features
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(documents)

# train Multinomial Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train, labels)

# function to classify text
def classify_with_bayes(texts: List[str]) -> List[str]:
  X_test = vectorizer.transform(texts)
  predicted_labels = clf.predict(X_test)
  return predicted_labels

texts_to_classify = [
    "Ukraine, a country in Eastern Europe, has a rich cultural heritage and a diverse landscape.",
    "The situation in Ukraine has been a topic of international concern, with ongoing political and territorial disputes.",
    "Football, also known as soccer in some parts of the world, is a globally beloved sport with a massive following.",
    "Theano is a deep learning framework, widely recognized for its contributions to machine learning and artificial intelligence.",
]

predicted_categories = classify_with_bayes(texts_to_classify)

for text, category in zip(texts_to_classify, predicted_categories):
  print(f"Text: {text}")
  print(f"Predicted Category: {category}")

