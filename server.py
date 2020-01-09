from flask import Flask, render_template, redirect, request
from data_manager import *

app = Flask(__name__)

save_question = []

@app.route('/')
def route_index():
    table = question_list()
    return render_template('list.html', table=table)


@app.route('/question/<question_id>')
def route_question(question_id=None):
    table = question_list()
    answers = answer_list()
    return render_template('question.html', question_id=question_id, table=table, answers=answers)


@app.route('/add-question', methods=['GET', 'POST'])
def route_add_question():
    if request.method == 'POST':
        save_question.append(request.form['Your Question'])
        save_question.append(request.form['Your Comment'])
        print(save_question[0], save_question[1])
        return redirect('/')
    return render_template('add-question.html')


@app.route('/question/<question_id>/new-answer')
def route_new_answer():
    return render_template('new-answer.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)