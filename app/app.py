from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Pipeline is working successfully! Enes Yakışık Test"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
ß