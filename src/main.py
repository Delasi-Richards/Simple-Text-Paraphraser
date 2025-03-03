"""
This will be the main file.
The goal of this project is to design a spaCy model which will refactor words for their synonyms

Each sentence will be broken down to the words that make it up.
Then the synonyms for each word will be generated. This will only apply to nouns, adjectives and verbs.
If the synonym passes some tests, then it will be accepted.
The tests are: synonym similarity testing, and part of speech testing.
"""

import spacy
from nltk.corpus import wordnet


def get_synonyms(term):
	synonyms = set()  # Sets use less memory, and order is not important
	for syn in wordnet.synsets(term):
		for lemma in syn.lemmas():
			synonyms.add(lemma.name().replace("_", " "))
	return synonyms


def rewrite(sentence: str):
	nlp = spacy.load("en_core_web_lg")
	sentence_doc = nlp(sentence)
	for i in range(0, len(sentence_doc)):  # Parse every word in the sentence
		# print(f"Name: {doc[i].text} \t Part of Speech: {doc[i].pos_} \t Lemma: {doc[i].lemma_}")

		# Filter out words whose synonyms are to be generated
		if sentence_doc[i].pos_ == "NOUN" or sentence_doc[i].pos_ == "VERB" or sentence_doc[i].pos_ == "ADJ":

			synonyms = [j for j in get_synonyms(sentence_doc[i].text)]  # Generate synonyms into a list variable
			for j in range(0, len(synonyms)):  # This takes each synonym from the list of synonyms

				# This block of code creates a sentence with the current word swapped with a synonym
				syn_sentence_list = sentence_doc.text.split()
				syn_sentence_list[i] = synonyms[j]  # This is the list variable which holds the sentence with the synonym inserted

				# This block of code converts the list variable to a sentence variable
				syn_sentence = ""
				for k in syn_sentence_list:
					syn_sentence += (k + " ")

				# Check the similarity between the original sentence and the new sentence
				syn_sentence = nlp(syn_sentence)
				print(syn_sentence.text)
				print(sentence_doc.similarity(syn_sentence))


rewrite("The boy is here.")
# print(get_synonyms("car"))
