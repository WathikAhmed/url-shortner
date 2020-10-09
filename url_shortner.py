import hashlib  # For hashing the urls
import urllib   # For URL parsing to HTTP
from flask import Flask, url_for, redirect  # For Flask web hosting server


    
    
    
userInput = "z"
userInputUrl=""
myDatabase = {}



def hashFunc(word):
    sha = hashlib.sha256()
    sha.update(word.encode())
    return sha.hexdigest()[0:5]

def shortenUrl(urlString):
    if urlString not in myDatabase:
        myDatabase[urlString] =  hashFunc(urlString)
    return myDatabase[urlString]
    
def lengthenUrl(shortUrlString):
    for key, value in myDatabase.items():
        if value == shortUrlString:
            return key
    return "www.google.com"

def appendHTTP(my_url):
    p = urllib.parse.urlparse(my_url, 'http')
    netloc = p.netloc or p.path
    path = p.path if p.netloc else ''
    if not netloc.startswith('www.'):
        netloc = 'www.' + netloc

    p = urllib.parse.ParseResult('http', netloc, path, *p[3:])
    return p.geturl()
    
    
app = Flask(__name__)

@app.route("/short/<variable>")
def shortUrl(variable):
    return shortenUrl(variable)
    
@app.route("/<variable>")
def longUrl(variable):
    return redirect(appendHTTP(lengthenUrl(variable)))
    
if __name__ == '__main__':
    app.run(host= '192.168.0.58', port=8080, debug=True)
    

    
    
   

