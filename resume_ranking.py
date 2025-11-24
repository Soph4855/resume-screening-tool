import sys
import json
import nltk
from nltk.corpus import wordnet

######################### Functions #########################

# Takes in a word and returns list of synonyms (using nltk's wordnet corpus)
def list_synonyms(word):
    synonyms = set()
    for synonym in wordnet.synsets(word):
        for lemma in synonym.lemmas():
            synonyms.add(lemma.name())
    return list(synonyms)


# Takes in (preprocessed) resume path and returns resume in string format
def resume_loader(f):
    try:
        with open(f, 'r') as file:
            resume = file.read()
    except FileNotFoundError:
        print(f"Error: The file {f} was not found")
    except Exception as e:
        print(f"Exception: {e}")
    return resume


# Takes in json file with job qualifications and name of desired reqs list. Returns reqs list from file
def return_reqs_list(f, reqs):
    with open(f, 'r') as file:
        data = json.load(file)
    return data.get(reqs)


# Takes in resume string and job qualifications file. Returns True if potential candidate, False otherwise
def potential_candidate(resume, quals):
    hard_reqs = return_reqs_list(quals, "hard_reqs")
    soft_reqs = return_reqs_list(quals, "soft_reqs")

    for req in hard_reqs:
        if req not in resume:
            return False

    for req in soft_reqs:
        synonyms = list_synonyms(req)
        for synonym in synonyms:
            if synonym in resume:
                return True

    return False

#############################################################

def main(args):

    if len(args) == 1:
        print("Incorrect usage. Needs one additional argument: json file with candidate requirements")
        sys.exit()
    elif len(args) == 2:
        reqs = args[1]
    else:
        print("Incorrect usage/number of arguments")
        sys.exit()

    # Resume dataset
    f1 = 'processed_resumes/r1_p.txt'
    f2 = 'processed_resumes/r2_p.txt'
    f3 = 'processed_resumes/r3_p.txt'
    f4 = 'processed_resumes/r4_p.txt'
    f5 = 'processed_resumes/r5_p.txt'
    f6 = 'processed_resumes/r6_p.txt'
    f7 = 'processed_resumes/r7_p.txt'
    f8 = 'processed_resumes/r8_p.txt'
    
    # Resumes as strings
    s1 = resume_loader(f1)
    s2 = resume_loader(f2)
    s3 = resume_loader(f3)
    s4 = resume_loader(f4)
    s5 = resume_loader(f5)
    s6 = resume_loader(f6)
    s7 = resume_loader(f7)
    s8 = resume_loader(f8)

    # All resumes as a list of strings
    all_resumes = []
    all_resumes.append(s1)
    all_resumes.append(s2)
    all_resumes.append(s3)
    all_resumes.append(s4)
    all_resumes.append(s5)
    all_resumes.append(s6)
    all_resumes.append(s7)
    all_resumes.append(s8)

    
    candidates = []
    for i in range(len(all_resumes)):
        if potential_candidate(all_resumes[i], reqs):
            print(f"Candidate {i + 1} passed.")
            candidates.append(i + 1)

    
if __name__ == "__main__":
    main(sys.argv)
