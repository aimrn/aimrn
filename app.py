import os

from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    raw_questions = [
        "",  # We will waste the zeroth index 
        "My mind has never been sharper.",
        "I need less sleep than usual.",
        "I have so many plans and new ideas that it is hard for me to work.",
        "I feel a pressure to talk and talk.",
        "I have been particularly happy.",
        "I have been more active than usual.",
        "I talk so fast that people have a hard time keeping up with me.",
        "I have more new ideas than I can handle.",
        "I have been irritable."
        "It's easy for me to think of jokes and funny stories.",
        'I have been feeling like "life of the party".',
        "I have been full of energy.",
        "I have been thinking about sex.",
        "I have been feeling particularly playful.",
        "I have special plans for the world.",
        "I have been spending too much money.",
        "My attention keeps jumping from one idea to another.",
        "I find it hard to slow down and stay in one place.",
    ]
    questions = [{"num": str(index), "question": element} for index, element in enumerate(raw_questions)]
    questions = questions[1:]  # Waste the zeroth index

    return render_template("index.html", questions=questions)
