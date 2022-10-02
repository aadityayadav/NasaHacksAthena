![alt text](https://github.com/aadityayadav/NasaHacksAthena/blob/master/apps/static/assets/img/athena_logo.jpeg)
# ATHENA: Can AI predict our science legacy

## Introduction
This is a web-app created for the NASA Space Challenge (https://www.spaceappschallenge.org/). <br />
It uses advanced NLP models to perform abstractive summarization on research pdfs


## What exactly does it do?
Our software solves the challenge of "Can AI preserve our science legacy". We have successfully used NLPs to provide a useful and comprehensive overview of any NASA research without having to go through, or even open the research papers.

## How does it work?
For testing out our model, We have already uploaded a bunch of pdfs extracted from the NTRS database. You can choose any of the available pdfs on the website and easily test our model. Upon selecting a pdf, you will see the summary along with the top keywords appear on the screen. If the summary aligns with your research needs, you can use the associated keywords to find more such related pdfs.
NOTE: Many of NASA's pdfs are not stored in the right format, they are very blurry scanned images which are difficult to extract. Due to the time constraints of this hackathon, we have built our NLP for well documented pdfs. However, an NER recognition NLP can be integrated in this project's pipeline if it were to be expanded.


##What benefits does it have?
This saves researchers a lot of time. If this was to be integrated with the NTRS database, then it can use its API to dynamically pick pdfs (instead of us having pdfs uploaded on the front-end, which we have done right now for ease of testing our project).


## What do you hope to achieve?
We hope that this software will have a positive impact on the usability of the NTRS database. We sincerely believe that this will greatly ease the work of researchers who are trying to skim through researches to decide which one suits them the most.


## What tools, coding languages, hardware, or software did you use to develop your project?
For the model, We used HuggingFace's extensive NLP library to understand what suits our needs for abstractive summarization and keyword extraction. For the backend, we used Flask to integrate all our components together along with HTML and CSS for the front end


## Creators
This web app is created by Ojas Sharma and Aaditya Yadav.
