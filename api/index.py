from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>My Vercel Website</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    max-width: 800px;
                    margin: 0 auto;
                    padding: 20px;
                    text-align: center;
                }
                h1 { color: #333; }
            </style>
        </head>
        <body>
            <h1>Welcome to My Vercel Website!</h1>
            <p>This is a simple Python website deployed on Vercel.</p>
        </body>
    </html>
    """

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Python!"})

if __name__ == '__main__':
    app.run()