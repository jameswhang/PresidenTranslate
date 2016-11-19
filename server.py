from flask import Flask, render_template, url_for, request
from flask_cors import CORS, cross_origin

from translation_service import TranslationService

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/translate/<word>')
def translate_test(word):
    ts = TranslationService('T')
    return ts.translate(word)

@app.route('/translate', methods=['POST'])
@cross_origin()
def translate():
    req_text = request.form['translateText']
    president = request.form['president']
    ts = TranslationService(president)
    translated = ts.translate(req_text)
    return translated
