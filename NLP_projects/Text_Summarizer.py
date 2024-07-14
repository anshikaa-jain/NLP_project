import nltk 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

#Adding text here for summarizing..  
text_for_summarization = "Natural Language Processing (NLP) is a branch of Artificial Intelligence dedicated to the study of how humans process the information that comes to us through language. It is a very complex area of research, as language is a very powerful tool for communicating and transmitting the information. Natural Language Processing systems try to emulate the way humans process information, eg. they strive to analyze the meaning of words and construct a representation of the world that allows us to interpret language naturally. Advances in this field of Artificial Intelligence have made it possible to develop systems that are capable of understanding language in a relatively natural way. Libraries used for NLP are spaCy. NLTK and many more."

# Tokenizing the text and setting stopwords..
stop_words = set(stopwords.words("english")) 
words = word_tokenize(text_for_summarization) 
   
# Creating a frequency table to keep the score of each word 
   
words_freq_table = dict() 
for word in words: 
    word = word.lower() 
    if word in stop_words: 
        continue
    if word in words_freq_table: 
        words_freq_table[word] += 1
    else: 
        words_freq_table[word] = 1
   
# Creating a dictionary to keep the score of each sentence 
sentences = sent_tokenize(text_for_summarization) 
sentences_freq_table = dict() 
   
for sentence in sentences: 
    for word, freq in words_freq_table.items(): 
        if word in sentence.lower(): 
            if sentence in sentences_freq_table: 
                sentences_freq_table[sentence] += freq 
            else: 
                sentences_freq_table[sentence] = freq 
   
   
   
sum_values = 0
for sentence in sentences_freq_table: 
    sum_values += sentences_freq_table[sentence] 
   
# Average value of a sentence from the original text 
average = int(sum_values / len(sentences_freq_table)) 
print(average)
   
# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
    if (sentence in sentences_freq_table) and (sentences_freq_table[sentence] > (1.1 * average)): 
        summary += " " + sentence 
print(summary)  
