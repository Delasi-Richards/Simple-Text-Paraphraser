"""
This will hold the functions for searching for synonyms, and rephrasing
get_synonyms() -> Gets synonyms from wordnet.
rewrite() -> Inserts synonyms into the sentence
test() -> Check if the new sentence can replace the old sentence based on its similarity score
"""

import spacy
from nltk.corpus import wordnet as wn

nlp = spacy.load("en_core_web_lg")


def get_synonyms(term):
	synonyms_set = set()  # Don't have to worry about duplicate entries
	for a in wn.synsets(term):
		for b in a.lemmas():
			synonyms_set.add(b.name().replace("_", " "))
	synonyms = [i for i in synonyms_set]
	return synonyms


def rewrite(sentence: str, index: int) -> list[str]:
	"""
	Inserts synonyms for the word at index into the sentence inputted
	:param sentence: Sentence to be changed
	:param index: The index of the word to be replaced in the sentence
	:return: List of sentences with the original word swapped out
	"""
	syn_sentences = []  # Return list

	sentence_doc = nlp(sentence)
	synonyms = get_synonyms(sentence_doc[index].text)  # Get synonyms for the word to be replaced

	for i in range(0, len(synonyms)):  # This takes each synonym from the list of synonyms
		if sentence_doc[index].text != synonyms[i] and sentence_doc[index].pos == nlp(synonyms[i])[-1].pos:
			# If the synonym is not the same as the OG word and has the same part of speech
			syn_sentence = sentence_doc.text  # The original sentence
			syn_sentence = syn_sentence.replace(sentence_doc[index].text, synonyms[i])  # Replacing the word with a synonym
			syn_sentences.append(syn_sentence)  # Add the new sentence to the return list

	return syn_sentences


def test(org_sentence: str, syn_sentences: list[str]) -> list[float]:
	"""
	Checks each sentence in the synonymous sentences list against the original, and give a similarity score
	:param org_sentence: The original sentence
	:param syn_sentences: List containing the similarity scores
	:return: A dictionary with the score for each word
	"""
	scores = []
	org_doc = nlp(org_sentence)
	for i in range(0, len(syn_sentences)):
		syn_sentence = nlp(syn_sentences[i])
		scores.append(org_doc.similarity(syn_sentence))

	return scores


# Deprecated
def rewrite1(sentence: str):
	nlp = spacy.load("en_core_web_lg")
	sentence_doc = nlp(sentence)
	for i in range(0, len(sentence_doc)):  # Parse every word in the sentence
		# print(f"Name: {sentence_doc[i].text} \t Part of Speech: {sentence_doc[i].pos_} \t Lemma: {sentence_doc[i].lemma_}")

		# Filter out words whose synonyms are to be generated
		if sentence_doc[i].pos_ == "NOUN" or sentence_doc[i].pos_ == "VERB" or sentence_doc[i].pos_ == "ADJ" or sentence_doc[i].pos_ == "ADV":

			synonyms = [j for j in get_synonyms(sentence_doc[i].text)]  # Generate synonyms into a list variable
			# print(f"{sentence_doc[i]}: {synonyms}")  # Test to check the synonyms

			for j in range(0, len(synonyms)):  # This takes each synonym from the list of synonyms

				# This block of code creates a sentence with the current word swapped with a synonym
				# It first checks that the synonym is not the same as the original word, and that they are the same POS
				# If the check passes, the new sentence is checked
				syn_sentence_list = sentence_doc.text.split()
				print(f"Original Word: {sentence_doc[i].pos_} \t New Word: {nlp(synonyms[j])[-1].pos_}")
				if syn_sentence_list[i] != synonyms[j] and sentence_doc[i].pos == nlp(synonyms[j])[-1].pos:
					syn_sentence_list[i] = synonyms[j]  # This is the list variable which holds the sentence with the synonym inserted

					# This block of code converts the list variable to a sentence variable
					syn_sentence = ""
					for k in syn_sentence_list:
						syn_sentence += (k + " ")

					# Check the similarity between the original sentence and the new sentence
					syn_sentence = nlp(syn_sentence)
					print(syn_sentence.text)
					# print(sentence_doc.similarity(syn_sentence))


new = rewrite("The boy is here", 1)
new_scores = test("The boy is here", new)
print(new)
print(new_scores)
