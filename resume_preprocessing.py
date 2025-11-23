import sys
import nltk
import re
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from gensim.models import Word2Vec

# nltk.download('punkt_tab') # a model for splitting text into sentences
# nltk.download('stopwords') # list of 'useless' words ('a', 'an', etc.)
# nltk.download('averaged_perceptron_tagger') # for pos tagging
# nltk.download('averaged_perceptron_tagger_eng') # for pos tagging
# nltk.download('wordnet') # for synonym relationships

######################### Functions #########################

def get_wn_pos(tb_tag):
    if tb_tag.startswith('J'):
        return wordnet.ADJ
    elif tb_tag.startswith('V'):
        return wordnet.VERB
    elif tb_tag.startswith('N'):
        return wordnet.NOUN
    elif tb_tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''

#############################################################

def main(args):
    
    # Read in file name from command line
    if len(sys.argv) == 1:
        print("Missing second argument: resume as .txt file")
        sys.exit()
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print("Incorrect usage")
    

    stop_words = set(stopwords.words('english'))
    
    with open(filename, 'r', encoding='utf-8') as file:
        resume = file.read()
    
    # Tokenize
    words = word_tokenize(resume)
    
    # Lowercase and remove stopwords/unnecessary punctuation
    words_list = [w.lower() for w in words if w.lower() not in stop_words]
    
    cleaned_tokens = []
    for w in words_list:
       w = re.sub(r'[^\w+]', '', w)
       if w:
           cleaned_tokens.append(w)
    
    '''
    # Lemmatize
    lemmatizer = WordNetLemmatizer()
    
    tagged_tokens = nltk.pos_tag(cleaned_tokens)
    
    tb_tags = []
    for token, tag in tagged_tokens:
        tb_tags.append(tag)
    
    final_words = []
    
    for i in range(len(tb_tags)):
        if get_wn_pos(tb_tags[i]):
            final_words.append(lemmatizer.lemmatize(cleaned_tokens[i], get_wn_pos(tb_tags[i])))
        else:
            final_words.append(cleaned_tokens[i])
    '''
   
    # Rather than printing cleaned_tokens, dump them into file in 'processed_resumes' directory

    print(cleaned_tokens)


if __name__ == "__main__":
    main(sys.argv)

