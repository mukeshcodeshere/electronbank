from flask import Flask, jsonify, render_template
from flask import send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Python!"})

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# This is the entry point for Vercel serverless functions
def handler(request):
    """Handle incoming requests and return a response"""
    with app.test_request_context(request.url):
        return app.full_dispatch_request()
