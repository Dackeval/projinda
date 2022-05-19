import fasttext
from flask import Flask, render_template, request


model = fasttext.load_model("lid.176.bin")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Website-DD1349.html')

@app.route('/', methods=['POST'])

def getvalue():
    input = request.form['input']
    answer = (model.predict(input))
    return render_template('pass.html', n=answer)


if __name__ == '__main__':
    app.run(debug=True)


