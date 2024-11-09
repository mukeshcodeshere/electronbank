from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Electron Bank - Future == Technology</title>
            <style>
                body {
                    font-family: 'Arial', sans-serif;
                    margin: 0;
                    padding: 0;
                    background-color: #ffffff;
                    color: #000000;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    text-align: center;
                }
                .container {
                    max-width: 900px;
                    margin: 0 auto;
                    padding: 40px;
                    border: 1px solid #ccc;
                    border-radius: 10px;
                }
                h1 {
                    font-size: 3rem;
                    color: #000000;
                    margin-bottom: 10px;
                }
                p {
                    font-size: 1.25rem;
                    color: #333;
                    margin-top: 20px;
                }
                .slogan {
                    font-size: 1.5rem;
                    color: #555;
                    margin-top: 30px;
                    font-style: italic;
                }
                .logo {
                    width: 150px;
                    height: auto;
                    margin-bottom: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <img class="logo" src="/static/logo.png" alt="Electron Bank Logo">
                <h1>Welcome to Electron Bank</h1>
                <p>Your partner in navigating the future of finance.</p>
                <p class="slogan">Future == Technology</p>
            </div>
        </body>
    </html>
    """

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello from Python!"})

if __name__ == '__main__':
    app.run(debug=True)
