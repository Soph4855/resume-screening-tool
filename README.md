# resume-screening-tool
A tool for screening resumes based on required job qualifications. 

## Requirements
Python must be installed on your local machine. Other required packages include (pip installation recommended):
* nltk
* gensim

## Usage
This tool is usable at the command-line interface. The main components are:
* A dataset of .txt resume files
* .json files containing job qualifications (located in `resume-screening-tool/required_skills`)
* `resume-screening-tool/resume_ranking.py`, the script that saves and prints a list of candidates who passed the resume screening

When in the directory `resume-screening-tool/`, run the tool using the following command-line arguments:
`python resume_ranking.py <qualifications file>`
This will output a list of candidates who passed the screening, where the "candidate" is simply the number of the resume that passed. 

### Example Usage
`$ python resume_ranking.py required_skills/ex3_hr.json`
>> Candidate 3 passed.
>> Candidate 7 passed.

## Dataset
The dataset (`resume-screening-tool/resume_dataset`) contains eight sample resume files, drawn from Bellevue University Career Services. The original link with all resumes is [here](https://msnlabs.com/img/resume-sample.pdf). (Note that only the one-page resumes were included in the `resume-screening-tool-resume_dataset` folder). The tool is not specific to these resumes--it should work with any chosen resume files. This would require:
1. Downloading resumes, converting them to .txt format, and storing them in a folder
2. Adding that folder to the repo
3. Changing the resume file paths in `resume-screening-tool/resume_preprocessing.py` and `resume-screening-tool/resume_ranking.py` to the new resume file paths. 
