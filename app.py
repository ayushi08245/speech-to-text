from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

speech_data = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/save", methods=["POST"])
def save_text():
    data = request.json
    text = data.get("text")
    
    speech_data.append(text)

    return jsonify({"message": "Text saved successfully"})

if __name__ == "__main__":
    app.run(debug=True)