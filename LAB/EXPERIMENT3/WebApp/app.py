from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Experiment 3: Deploying Web Applications with Docker</h1>
    <h2>Angel- SAP ID: 500119630</h2>
    <h2>Nakul - SAP ID: 500121882</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)