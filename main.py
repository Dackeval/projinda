import fasttext
from flask import Flask, render_template, request

language_dict = {'af': 'Afrikaans',
                 'sv': 'Swedish',
                 "als": "Tosk Albanian",
                 "am": "Amharic",
                 "an": "Aragonese",
                 "ar": "Arabic",
                 "arz": "Egyptian Arabic",
                 "as": "Assamese",
                 "ast": "Asturian",
                 "av": "Avaric",
                 "az": "Azerbaijani",
                 "azb": "South Azerbaijani",
                 "ba": "Bashkir",
                 "bar": "Bavarian",
                 "bcl": "Central Bikol",
                 "be": "Belarusian",
                 "bg": "Bulgarian",
                 "bh": "Bihari",
                 "bn": "Bengali",
                 "bo": "Tibetan",
                 "bpy": "Bishnupriya Manipuri",
                 "br": "Breton",
                 "bs": "Bosnian",
                 "ca": "Catalan",
                 "cbk": "Zamboanga Chavacano",
                 "ce": "Chechen",
                 "ceb": "Cebuano",
                 "ckb": "Central Kurdish",
                 "co": "Corsican",
                 "cs": "Czech",
                 "da": "Danish",
                 "de": "German",
                 "el": "Greek",
                 "en": "English",
                 "es": "Spanish",
                 "et": "Estonian",
                 "eu": "Basque",
                 "fa": "Persian",
                 "fi": "Finnish",
                 "fr": "French",
                 "ga": "Irish",
                 "gl": "Galician",
                 "he": "Hebrew",
                 "hi": "Hindi",
                 "hr": "Croatian",
                 "is": "Icelandic",
                 "it": "Italian",
                 "ko": "Korean",
                 "ku": "Kurdish",
                 "la": "Latin",
                 "lt": "Lithuanian",
                 "lv": "Latvian",
                 "nl": "Dutch",
                 "no": "Norweigian",
                 "pl": "Polish",
                 "pt": "Portuguese",
                 "ro": "Romanian",
                 "ru": "Russian",
                 "sa": "Sanskrit",
                 "sl": "Slovenian",
                 "so": "Somali",
                 "sr": "Serbian",
                 "su": "Sundanese",
                 "ta": "Tamil",
                 "tr": "Turkish",
                 "uk": "Ukrainian",
                 "vi": "Vietnamese",
                 "vo": "Volapük",
                 "wa": "Walloon",
                 "yi": "Yiddish",
                 "yo": "Yoruba",
                 }

model = fasttext.load_model("lid.176.bin")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Website-DD1349.html')

@app.route('/', methods=['POST'])

def getvalue():
    input = request.form['input']
    answer = (model.predict(input))
    answerr = str(answer[0])
    answerr = answerr.replace("'__label__", '')
    answerr = answerr.replace("'", "")
    answerr = answerr.replace(",", "")
    answerr = answerr.replace("(", "")
    answerr = answerr.replace(")", "")
    send = "Your input is written in: " + language_dict[answerr]
    return render_template('pass.html', n=send)


if __name__ == '__main__':
    app.run(debug=True)




