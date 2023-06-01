# PROBLEM 3:Removes usless words and provides an API for the same
# for running, type uvicorn problem3:app --reload in the terminal
# from the terminal copy the url and paste it in the browser
# in the browser, add /?text= and then the text you want to analyze

import string
import nltk
from fastapi import FastAPI
app = FastAPI()
stopwords = nltk.corpus.stopwords.words('english')
c = ['what', 'when', 'how', 'where', 'why', 'of','to']
for a in c: 
    stopwords.remove(a)
    

@app.get("/")
async def root(text: str):
    text_a = text.split(" ")
    text_new = "".join([i for i in text if i not in string.punctuation])
    words = nltk.tokenize.word_tokenize(text_new)
    words_new = [i for i in words if i not in stopwords]
    a = " ".join(str(a) for a in words_new)
    b = {
        "text": a,
        "o_length": len(words_new),
        "i_length": len(text_a),
        "reduced": len(text_a) - len(words_new),
    }
    return b
