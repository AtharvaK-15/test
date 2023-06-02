# # PROBLEM 3:Removes usless words and provides an API for the same
# # for running, type uvicorn problem3:app --reload in the terminal
# # from the terminal copy the url and paste it in the browser
# # in the browser, add /?text= and then the text you want to analyze

# # import string
# # import nltk
# from fastapi import FastAPI
# app = FastAPI()
# import nltk
# import bs4 as bs
# import urllib.request
# import re
# # stopwords = nltk.corpus.stopwords.words('english')
# # c = ['what', 'when', 'how', 'where', 'why', 'of','to']
# # for a in c:
# #     stopwords.remove(a)


# @app.get("/")
# async def root(text: str):
# #     text_a = text.split(" ")
# #     text_new = "".join([i for i in text if i not in string.punctuation])
# #     words = nltk.tokenize.word_tokenize(text_new)
# #     words_new = [i for i in words if i not in stopwords]
# #     a = " ".join(str(a) for a in words_new)
# #     b = {
# #         "text": a,
# #         "o_length": len(words_new),
# #         "i_length": len(text_a),
# #         "reduced": len(text_a) - len(words_new),
# #     }
# #     return b
#     scraped_data = "open function from the urllib.request utility to scrape the data. Next, we need to call read function on the object returned by urlopen function in order to read the data. To parse the data, we use BeautifulSoup object and pass it the scraped data object i.e. article and the lxml parser.In Wikipedia articles, all the text for the article is enclosed inside the <p> tags. To retrieve the text we need to call find_all function on the object returned by the BeautifulSoup. The tag name is passed as a parameter to the function. The find_all function returns all the paragraphs in the article in the form of a list. All the paragraphs have been combined to recreate the article."
#     article = scraped_data.read()

#     parsed_article = bs.BeautifulSoup(article,'lxml')

#     paragraphs = parsed_article.find_all('p')

#     article_text = ""

#     for p in paragraphs:
#         article_text += p.text
        
#     article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
#     article_text = re.sub(r'\s+', ' ', article_text)
#     formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
#     formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
#     sentence_list = nltk.sent_tokenize(article_text)

#     stopwords = nltk.corpus.stopwords.words('english')

#     word_frequencies = {}
#     for word in nltk.word_tokenize(formatted_article_text):
#         if word not in stopwords:
#             if word not in word_frequencies.keys():
#                 word_frequencies[word] = 1
#             else:
#                 word_frequencies[word] += 1
                
#     maximum_frequncy = max(word_frequencies.values())

#     for word in word_frequencies.keys():
#         word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
        
#     sentence_scores = {}
#     for sent in sentence_list:
#         for word in nltk.word_tokenize(sent.lower()):
#             if word in word_frequencies.keys():
#                 if len(sent.split(' ')) < 30:
#                     if sent not in sentence_scores.keys():
#                         sentence_scores[sent] = word_frequencies[word]
#                     else:
#                         sentence_scores[sent] += word_frequencies[word]
                        
#     import heapq
#     summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

#     summary = ' '.join(summary_sentences)
#     print(summary)


import nltk
import bs4 as bs
import urllib.request
import re

scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = ""

for p in paragraphs:
    article_text += p.text
    
article_text = re.sub(r'\[[0-9]*\]', ' ', article_text)
article_text = re.sub(r'\s+', ' ', article_text)
formatted_article_text = re.sub('[^a-zA-Z]', ' ', article_text )
formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)
sentence_list = nltk.sent_tokenize(article_text)

stopwords = nltk.corpus.stopwords.words('english')

word_frequencies = {}
for word in nltk.word_tokenize(formatted_article_text):
    if word not in stopwords:
        if word not in word_frequencies.keys():
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
            
maximum_frequncy = max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)
    
sentence_scores = {}
for sent in sentence_list:
    for word in nltk.word_tokenize(sent.lower()):
        if word in word_frequencies.keys():
            if len(sent.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word]
                else:
                    sentence_scores[sent] += word_frequencies[word]
                    
import heapq
summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

summary = ' '.join(summary_sentences)
print(summary)