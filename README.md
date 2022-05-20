# projinda
Projinda 2022 - ML - Fasttext

Language identifier 

Introduction 

My idea is to build a basic website where a user is able to do a text input and get a return of what language the user is writing in. The code will make use of Facebooks NLP ML ”Fasttext”. Where I suppose most of my work will go into understanding, configuring & improving. 

What is NLP and ML ? 
NLP is short for Natural Language Processing and is a subfield of artificial intelligence (AI). It helps machines process and understand human languages so that it can do certain task with it. 
For example translating, summarization, ticket classification or spell checking. 

Machine learning (ML) is also a type of AI, which allows software applications to become more accurate at preticting outcomes without explicitly programming the software to do so. ML tend to need alot of "training data" to improve its precision. 


Main goals of the language identifier 

- Identify several different language inputs successfully
- Build a basic website for text entry and answer

The code will use:

Python as a base for the language identifier. 
HTML, CSS, JS for the website.
Installing Fasttext and Flask is also a requirement to be able to launch the website. 

How to use the website

Since the website will be hosted locally, the user first need to launch the main.py file in the repository.
To run the main.py file the user first need to enter in the terminal python main.py. The user will then be the address: http://127.0.0.1:5000, where the website then is launched. 

On the actual website the user is able to enter into the text-field whatever language the user wants to check for and press return. Once the user presses return the website will give a response on what language the model predicts this is. 


Discussion

Problems

I encountered a couple of difficulties when working with the project. My first bump to get over was to install and understand the ML fasttext module. It took me quite some time tto figure out how to actually iuse the module and be able to do anything of substance with it. My next hurdle was integrating the ML model with the website. There was supposedly an wedmodule for fasttext which I was supposed to be able to install to use for websites, but after many hours of error message handeling and help from KTH assistance. I gave up on that Idea and used a python module for fasttext combined with Flask an python Module to be able to send data back and forth inbetween python and HTML files. 

Aside from these issues I also encountered git's large file detected problem. Which led me to use Gits Rebase feature to be able to clear out old commits from the history and then use git stash to be able to connect the conflicting histories in my local rep and the remote rep. 


Things learned

So there was several things learnt during this project. I have never integrated an website and Python which is a useful experience to have learnt. I have also never encountered the large file detected problem on GIT which made me understand how git saves histories of your past commits and how to clear them and then again connect the conflicting histories on GIT. 

ML was also an completely new field for me to work within. The fasttext module is very simple once everything is installed and up and running, but getting everything working wasn't the easiest. It was a fun and intresting journey to learn how to construct models and use them. 


Links

https://fasttext.cc/docs/en/support.html - How to download Fasttext and create & build models 

https://fasttext.cc/docs/en/unsupervised-tutorial.html - building wordvectors 

https://www.youtube.com/watch?v=j-k6uU5yYHU - Passing information from python to HTML and vice verse 

https://git-scm.com/docs/git-rebase - Git rebase info



Author 

Sigvard Dackevall
