import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template, request

app = Flask(__name__)

def cleanMe(html):
    soup = BeautifulSoup(html, features='html.parser') # create a new bs4 object from the html data loaded
    soup = BeautifulSoup(soup.prettify(), features='html.parser')
    for script in soup(['script', 'style']): # remove all javascript and stylesheet code
        script.extract()
    # get text
    text = soup.get_text()
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)
    return text



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/strip', methods=['POST'])
def clean():
    payload = request.get_json()
    text = ''
    if payload.get('url'):
        text = requests.get(payload.get('url')).text
        return cleanMe(text)
    if payload.get('xml'):
        text = payload.get('xml', '')
        return cleanMe(text)
