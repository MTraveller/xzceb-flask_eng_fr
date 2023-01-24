""" Translation server and endpoints """
from flask import Flask, render_template, request
from machinetranslation.translator import english_to_french, french_to_english

app = Flask("Web Translator",
            static_folder="./final_project/static",
            template_folder="./final_project/templates")


@app.route("/englishToFrench")
def englishToErench():
    """ Translate english to french """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    print(textToTranslate)

    return english_to_french(textToTranslate)


@app.route("/frenchToEnglish")
def frenchToEnglish():
    """ Translate french to english """
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return french_to_english(textToTranslate)


@app.route("/")
def renderIndexPage():
    """ Render index page """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8082)
