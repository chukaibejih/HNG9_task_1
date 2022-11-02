from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bio = [
    {   "slackUsername": "Ibejih", 
        "backend": True, 
        "age": 22, 
        "bio": "As a young backend developer, I am very enthusiastic I enjoy getting my hands on new projects and love learning. My current tech stack is Python (Django and Flask frameworks and APIs), PostgreSQL, HTML and CSS." 
    }
]

@app.route("/")
def get_bio():
    return jsonify(bio)

    