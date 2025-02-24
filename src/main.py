"""
This will be the main file.
The goal of this project is to design a spaCy model which will refactor words for their synonyms

Each sentence will be broken down to the words that make it up.
Then the synonyms for each word will be generated. This will only apply to nouns, adjectives and verbs.
If the synonym passes some tests, then it will be accepted.
The tests are: synonym similarity testing, and part of speech testing.
"""

import spacy


def rewrite(sentence: str):
	nlp = spacy.load("en_core_web_sm")
	doc = nlp(sentence)
	for i in range(0, len(doc)):
		# print(f"Name: {doc[i].text} \t Part of Speech: {doc[i].pos_} \t Lemma: {doc[i].lemma_}")

		if doc[i].pos_ == "NOUN" or doc[i].pos_ == "VERB" or doc[i].pos_ == "ADJ":
			print("pass")


rewrite("The boy is washing the car")
