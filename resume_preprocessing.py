import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

with open('resume_dataset/r1.txt', 'r', encoding='utf-8') as file:
    r1 = file.read()

nltk.download('punkt_tab') # a model for splitting text into sentences

words = word_tokenize(r1)
sentences = sent_tokenize(r1)

print(words)
print(sentences)
