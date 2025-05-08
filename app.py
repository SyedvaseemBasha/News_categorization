# app.py
from flask import Flask, request, jsonify, render_template
from backend.model import classify_news_article

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    article = data.get("query", "")
    if not article.strip():
        return jsonify({"response": "Please enter a valid news article."})
    try:
        category = classify_news_article(article)
        return jsonify({"response": f"{category}"})
    except Exception as e:
        return jsonify({"response": f"Decrease the length of the article.:)"})
        # return jsonify({"response": f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(debug=True)
