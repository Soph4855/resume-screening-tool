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

def main(args):
    
    # Read in file name from command line
    if len(sys.argv) == 1:
        print("Missing second and third arguments: resume as .txt file, output file (.txt) for processed resume")
        sys.exit()
    elif len(sys.argv) == 2:
        print("Missing third argument: output file (.txt) for processed resume")
        sys.exit()
    elif len(sys.argv) == 3:
        filename = sys.argv[1]
        outfile = sys.argv[2]
    else:
        print("Incorrect usage")
        sys.exit()
    

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
     
    # Dump tokens into file in 'processed_resumes' directory
    with open(outfile, 'w') as file:
        print(cleaned_tokens, file=file)


if __name__ == "__main__":
    main(sys.argv)

