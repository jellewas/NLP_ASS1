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


nlp = spacy.load("en_core_web_sm")

text = open("/Users/Colette/Downloads/intro2nlp_assignment1_code/data/preprocessed/train/sentences.txt").read()
doc = nlp(text)

"""
# 1 - Tokenization 
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
print(f'The average number of words per sentence is : {avg_nr_words}')

avg_word_len = word_len_counter/word_counter
print(f'The average length per word is : {avg_word_len}')


# 2 - word classes 
pos_frequencies = {}
kind_words = []

# count the occurences of every POS
for token in doc:
    if token.pos_ in pos_frequencies:
        pos_frequencies[token.pos_] += 1
    else:
        pos_frequencies[token.pos_] = 1
        #add the POS to a list such that we can loop over the list
        kind_words.append(token.pos_)

#Calculate the frequency os every POS
total_pos = sum(pos_frequencies.values())
for pos, value in pos_frequencies.items():
    print(f'Of this POS: {pos}, this is the relative frequency: {value/total_pos}')

#Loop over every POS and check for that POS what the most common and less common words are
for words in kind_words:
    kind_a = [token.text for token in doc if token.pos_ == words]
    word_freq = Counter(kind_a)
    common_words = word_freq.most_common(3)
    less_common_words = word_freq.most_common()[-1]

    print(f'For {words} these are the three most frequent words and the number they occur {common_words}')

    print(f'For {words} this is one of the less frequent words and the number it occurs {less_common_words}')

"""

# 3 N-Grams

#TOKEN BIGRAMS & TRIGRAMS
bigram_dic = dict()
bigram = []

trigram = []
trigram_dic = dict()

for token in doc[0:-1]:
    bigram.append(token)
    bigram.append(token.nbor())

    bigram_s = str(bigram)
    bigram_dic[bigram_s] = bigram_dic.get(bigram_s, 0) + 1

    if not token.i == doc[-2].i:
        trigram = bigram
        trigram.append(token.nbor(2))
        trigram = str(trigram)
        trigram_dic[trigram] = trigram_dic.get(trigram, 0) + 1

        bigram = []
        trigram = []

   
bigram_count = Counter(bigram_dic)
trigram_count = Counter(trigram_dic)
print("The most common bigram tokens are:", bigram_count.most_common(3))
print("The most common trigram tokens are:", trigram_count.most_common(3))

#SAME BI/TRI-GRAMS, BUT THEN FOR THE POS TAG 
bigram_dic = dict()
bigram = []

trigram = []
trigram_dic = dict()

for token in doc[0:-1]:
    #print(token.i, token, token.idx)
    bigram.append(token.pos_)
    bigram.append(token.nbor().pos_)

    bigram_s = str(bigram)
    bigram_dic[bigram_s] = bigram_dic.get(bigram_s, 0) + 1

    if not token.i == doc[-2].i:
        trigram = bigram
        trigram.append(token.nbor(2).pos_)
        trigram = str(trigram)
        trigram_dic[trigram] = trigram_dic.get(trigram, 0) + 1

        bigram = []
        trigram = []

   
bigram_count = Counter(bigram_dic)
trigram_count = Counter(trigram_dic)
print("The most common bigram tokens are:", bigram_count.most_common(3))
print("The most common trigram tokens are:", trigram_count.most_common(3))



#4 Print all the lemmatizations
# lemma_dict = {}
# sentence_dict = {}

# for sentence in doc.sents:
#     for token in sentence:        
#         if token.lemma_ in lemma_dict:
#             token_list = lemma_dict[token.lemma_]
#             if token.text not in token_list:
#                 lemma_dict[token.lemma_].append(token.text)
#                 sentence_dict[token.lemma_].append(sentence)
#         elif token.lemma_ not in lemma_dict:
#             lemma_dict[token.lemma_] = [token.text]
#             sentence_dict[token.lemma_] = [sentence]

# for key, value in lemma_dict.items():
#     if len(value) == 3:
#         print(key)
#         break

# #this is the key with 3 inlfections: age

# print(lemma_dict['age'])
# print(sentence_dict['age'])


# # 5 Named Entity Recognition

# number_entities = []
# number_labels = []

# for ent in doc.ents:
#     number_entities.append(ent.text)
#     number_labels.append(ent.label_)

# print(f'This is the number of unique entities: {len(set(number_entities))}')
# print(f'This is the number of unique labels: {len(set(number_labels))}')

# # print per sentence whether it is an entity and what kind of entity it is and .ent_iob_
# # prints “B” means the token begins an entity, 
# # “I” means it is inside an entity, “O” means it is outside an entity, 
# # and "" means no entity tag is set.
# # https://stackoverflow.com/questions/63283128/how-determine-if-a-token-is-part-of-an-entity-within-spacy
# sentence_counter = 0
# for sentence in doc.sents:
#     if sentence_counter == 5:
#         break

#     print(sentence)    
#     for token in sentence:
#         print(token, token.ent_type_, token.ent_iob_)
#     sentence_counter += 1

# PART B 
# 6 A
'''
The start value is the place at which the target word starts in the sentence. It is the place where the 
i'th charcater of the sentcence is (spaces, commas, etc.. included). The offset value is the place where 
the target word ends. Also, this is the i'th charcater of the sentence

'''
# B
'''
When a team participates in a probablistic classicfication task, the labels are assigned is a specifc manner:
<the number of annotators who marked the word as difficult>/<the total number of annotators>. A label of 0.4 means 
than that the <the total number of annotators> are 2.5 times more than the <the number of annotators who marked the word as difficult>

'''
# C
'''
The sixth and seventh columns show the number of native annotators and the number of non-native annotators who saw the sentence. 
The eighth and ninth columns show the number of native annotators and the number of non-native annotators who marked the target word
as difficult. (tot nu toe letterlijke copy paste maar wist het niet 100% zeker)
'''

# 7
filep_path = "data/original/english/WikiNews_Train.tsv"
final_df = pd.read_csv(filep_path, sep = '\t')

print(final_df)
