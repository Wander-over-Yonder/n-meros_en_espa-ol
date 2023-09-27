from flask import Flask
from flask import request
from flask import render_template

from num2words import num2words
from random import randint

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    max_number = 101
    correct_answers = int(request.args.get('correct', 0))
    incorrect_answers = int(request.args.get('incorrect', 0))
    user_answer = ''
    win = True

    n = int(request.args.get('n', -1))
    right_answer = num2words(n, lang='es')

    if request.method == 'POST':
        max_number = int(request.form.get('max_number', 101))
        user_answer = request.form.get('answer', '')
        if right_answer.lower() == user_answer.lower():
            correct_answers += 1
        else:
            incorrect_answers += 1
            win = False

    total_score = 0 + correct_answers + incorrect_answers
    n = randint(0, max_number)
    content = {'n': n,
               'text_to_speach': f'{num2words(n, lang="es")}',
               'max_number': max_number,
               'win': win,
               'right_answer': right_answer,
               'user_answer': user_answer,
               'total_score': total_score,
               'correct_answers': correct_answers,
               'incorrect_answers': incorrect_answers,
               }
    return render_template('index.html', content=content)
