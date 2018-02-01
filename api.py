import requests
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/api/crawler')
def crawler():
  url  = request.args.get('url')
  word = request.args.get('word')

  content = requests.get(url).text

  occurrences = content.count(word)

  return jsonify(
    url=url,
    word=word,
    occurrences=occurrences
  )