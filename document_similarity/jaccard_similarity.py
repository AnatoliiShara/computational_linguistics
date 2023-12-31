# -*- coding: utf-8 -*-
"""jaccard_similarity.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1INjV81KjNrukc2Q4bUFYoXgrZ-Fg5vz-
"""

!pip install spacy

import spacy
from typing import List, Tuple

nlp = spacy.load("en_core_web_sm")

base_document = "This is an example sentence for the document to be compared"
documents = [
    "This is the collection of documents to be compared against the base_document",
    "Politics can be a complex and divisive topic in society today.",
    "Sport brings people together and promotes a healthy lifestyle.",
    "Education is the key to unlocking a bright future for individuals.",
    "Kyiv, the capital of Ukraine, is known for its rich history and culture."
]

def preprocess(text: str) -> List[str]:
  # steps:
  # 1. lowercase
  # 2. lemmatize
  # 3. remove stopwords
  # 4. remove punctuation
  # 5. remove characters with a length of 1

  doc = nlp(text)
  words = []
  for token in doc:
    if not token.is_stop and not token.is_punct and len(token.text) > 1:
      words.append(token.lemma_.lower())
  return words

def calculate_jaccard(words_tokens1: List[str], word_tokens2: List[str]) -> float:
  both_tokens = words_tokens1 + word_tokens2
  union = set(both_tokens)
  # calculate intersection
  intersection = set(words_tokens1).intersection(word_tokens2)
  jaccard_score = len(intersection) / len(union)
  return jaccard_score

def process_jaccard_similarity():
  base_tokens = preprocess(base_document)

  # tokenize each document
  all_tokens = []
  for i, document in enumerate(documents):
    tokens = preprocess(document)
    all_tokens.append(tokens)

  all_scores = []
  for tokens in all_tokens:
    score = calculate_jaccard(base_tokens, tokens)
    all_scores.append(score)

  highest_score = max(all_scores)
  highest_score_index = all_scores.index(highest_score)
  most_similar_document = documents[highest_score_index]
  print("Most similar document by Jaccard with the score: ", most_similar_document, highest_score)
  print()

  lowest_score = min(all_scores)
  lowest_score_index = all_scores.index(lowest_score)
  least_similar_document = documents[lowest_score_index]
  print("Least similar document by Jaccard with the score: ", least_similar_document, lowest_score)
  print()

  print("\nKeyword pairs for the Most Similar Document:")
  for token in all_tokens[highest_score_index]:
    if token in base_tokens:
      print(token, end="")
  print()

  print("\nKeyword pairs for the Least Similar Document:")
  for token in all_tokens[lowest_score_index]:
    if token in base_tokens:
      print(token, end="")

process_jaccard_similarity()

