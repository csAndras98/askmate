from flask import Flask, render_template
from data_manager import *

app = Flask(__name__)



@app.route('/')
def route_list():
    table = element_table()
    return render_template('index.html')

@app.route('/list')
def route_index():
    table = element_table()
    table.remove(table[0])
    table.reverse()
    return render_template('list.html', table=table)



@app.route('/question/<question_id>')
def route_question():
    return render_template('question.html')


@app.route('/add-question')
def route_add_question():
    return render_template('add-question.html')


@app.route('/question/<question_id>/new-answer')
def route_new_answer():
    return render_template('new-answer.html')


if __name__ == '__main__':
    app.run(debug=True, port=5000)