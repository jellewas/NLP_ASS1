# Implement linguistic analyses using spacy
# Run them on data/preprocessed/train/sentences.txt
#en core web v.2.2, spacy v3.2

import spacy 
from collections import Counter
from collections import defaultdict
import operator
from itertools import tee


'''
1 & 2 (almost) ready

'''

# 1 - Tokenization 
nlp = spacy.load("en_core_web_sm")

text = open("/Users/jellewas/Documents/Master_Artificial_Intelligence/NLP/Assignment1/intro2nlp_assignment1_code/data/preprocessed/train/sentences.txt").read()
doc = nlp(text)

word_frequencies = Counter()
for sentence in doc.sents:
    words = []
    for token in sentence: 
        # Let's filter out punctuation
        if not token.is_punct:
            words.append(token.text)
    word_frequencies.update(words)
    

nr_of_tokens = text.__len__
nr_of_tokens_2 = len(doc)
print(f'The number of tokens are {nr_of_tokens_2}')
nr_of_types = len(word_frequencies.keys())
print(f'The number of types are {nr_of_types}')
nr_of_words = sum(word_frequencies.values())
print(f'The number of words are {nr_of_words}')

sentences = [i for i in doc.sents]

sentence_counter = 0
word_counter = 0
word_len_counter = 0

for sentence in sentences:
    words = []
    for token in sentence:
        if not token.is_punct:

            word_counter += 1
            word_len_counter += len(token)

    sentence_counter += 1

avg_nr_words = word_counter/sentence_counter
print(f'The average number of words per sentece is : {avg_nr_words}')

avg_word_len = word_len_counter/word_counter
print(f'The average length per word is : {avg_word_len}')

# 2 - word classes 
# pos_frequencies = {}
# kind_words = []

# # count the occurences of every POS
# for token in doc:
#     if token.pos_ in pos_frequencies:
#         pos_frequencies[token.pos_] += 1
#     else:
#         pos_frequencies[token.pos_] = 1
#         #add the POS to a list such that we can loop over the list
#         kind_words.append(token.pos_)

# #Calculate the frequency os every POS
# total_pos = sum(pos_frequencies.values())
# for pos, value in pos_frequencies.items():
#     print(f'Of this Pos: {pos}. This is the relative frequency: {value/total_pos}')

# #Loop over every POS and check for that POS what the most common and less common are
# for words in kind_words:
#     kind_a = [token.text for token in doc if token.pos_ == words]
#     word_freq = Counter(kind_a)
#     common_words = word_freq.most_common(3)
#     less_common_words = word_freq.most_common()[-1]

#     for common in common_words:
#         print(f'For {words} this is one of the most frequent words {common}')

#     for less_common in less_common_words:
#         print(f'For {words} this is one of the less frequent words {less_common}')


# 3 N-Grams
# https://www.depends-on-the-definition.com/introduction-n-gram-language-models/

tokenized = [x.text for x in doc]

def make_trigrams(iterator, n):
    if n == 2:
        a, b = tee(iterator, n)
        next(b)
        return zip(a, b)


    if n == 3:
        a, b, c = tee(iterator, n)
        next(b)
        next(c)
        next(c)
        return zip(a,b,c)

# get bigrams
bigrams = Counter(make_trigrams(tokenized, 2))
print(bigrams.most_common(3))

#get trigrams
bigrams = Counter(make_trigrams(tokenized, 3))
print(bigrams.most_common(3))
