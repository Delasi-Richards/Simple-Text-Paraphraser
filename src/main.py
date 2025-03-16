"""
The goal of this project is to design a spaCy model which will refactor words for their synonyms

Each sentence will be broken down to the words that make it up.
Then the synonyms for each word will be generated. This will only apply to nouns, adjectives and verbs.
If the synonym passes some tests, then it will be accepted.
The tests are: synonym similarity testing, and part of speech testing.

There are two files
1. main, where the main functionality is put together, input and output is handled here.
2. rewrite, where the rewriting, synonym generation and testing functions are
"""

from rewrite import nlp, rewrite, test

sentence = input("Enter the sentence here: ")
sentence_doc = nlp(sentence)

for i in range(0, len(sentence_doc)):
	print(sentence_doc[i].pos_)
	if sentence_doc[i].pos_ in ("NOUN", "VERB", "ADJ", "ADV"):
		syn_sentences = rewrite(sentence, i)  # Generate synonymous sentences
		scores = test(sentence, syn_sentences)  # Generate similarity scores for each sentence

		# Function to pick the largest score
		# Change rewrite() and test() to accept the Doc versions of "sentence" instead
