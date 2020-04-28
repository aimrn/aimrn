import os

from flask import Flask, render_template

app = Flask(__name__)
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

@app.route("/")
def index():
    # FIX: move this data out to a separate file so the app.py is less cluttered
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

    raw_second_questions = [
        # List should be increasing craziness/pathologicalness. It jumps down once you say yes to maybe three of them or something
        # Otherwise they keep appearing. Also you stop having the option of yes/no. it becoems just yes, then it becomes just the radio button
        "",  # Waste zeroth
        "Can you fix everything?",
        "Is everything amazing?",
        "Do you have a solution to all your problems?",
        "Is today the day your going to clean everything?",
        "And start running every day?",
        "And wake up early?",
        "And sleep by 10?",
        "Have you spent more than $100 today?",
        'Is your finger hovering over the bid button in eBay for a "...limited edition, special release, holo only first edition pokemon card complete set...',
        "Hold up, you have more than 20 tabs open right now?",
        "Did you sleep last night?",
        "WAIT, what do you mean /which night/ am I talking about? THATS EXACTLY THE PROBLEM 0_0",
        "YOU HAVEN'T SLEPT IN HOW MANY DAYS??",
        "IS THAT A PAINTBRUSH IN YOUR HAND??!!1",
        
    ]

    return render_template("index.html", questions=questions)

def faq():
    raq_qa = [
        {
            # FIX put a reverence number thing on the main page that links to here
            "question": "Do you have any data to back that up? I'm not manic.",
            "answer": "But are you though? :D In all seriousness yes I don't have any data to back it up. It's a joke. But I would surprised if there /wasn't/ a positive selection bias.",
        },
        {
            "question": "the question text",
            "answer": "the answer text",
        },
        {
            "question": "the question text",
            "answer": "the answer text",
        },

    ]


# TODO ROUTES
# about/why page
# contact page
# faq
# index for the paranoid
# yes(next page)
# no(next page)
    # maybe no just redirects to yes?
    # maybe with a funny something
    # dunno