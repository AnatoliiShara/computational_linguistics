# -*- coding: utf-8 -*-
"""document_similarity_word2vec.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16YXmwkvMImx2wuGt6j9naBVimEKEJ71q
"""

import gensim
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
import spacy

nlp = spacy.load("en_core_web_sm")

documents = [
    "This is the first document",
    "A quick brown fox jumps over the lazy dog.",
    "A lazy dog barks at the moon.",
    "Document similarity is important for many NLP tasks.",
    "Natural Language Processing (NLP) is a fascinating field."
]

# tokenize documents using SpaCy
tokenized_docs = [[token.text.lower() for token in nlp(doc)] for doc in documents]
tokenized_docs

# create tagged documents for training

tagged_data = [TaggedDocument(words=doc, tags=[str(i)]) for i, doc in enumerate(tokenized_docs)]
tagged_data

model = Doc2Vec(vector_size=20, # set dimensionality of document vectors
                window=2, # maximum distance between current and predicted word
                min_count=1, # ignores all words with total frequency lower than this
                epochs=100)

model.build_vocab(tagged_data)

model.train(tagged_data, total_examples=model.corpus_count, epochs=model.epochs)

# calculate the similarity between documents
for i in range(len(documents)):
  for j in range(i + 1, len(documents)):
    similarity = model.dv.similarity(str(i), str(j))
    print(f"Similarity between Document {i + 1} and Document {j + 1}: {similarity:.4f}")

