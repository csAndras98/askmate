import connection
import datetime

@connection.connection_handler
def get_all_questions(cursor):
    cursor.execute("""Select id, title, submission_time, message, view_number, vote_number from question """)
    questions = cursor.fetchall()
    return questions

@connection.connection_handler
def get_all_answer(cursor):
    cursor.execute("""Select id, message, submission_time, vote_number, question_id from answer """)
    answer = cursor.fetchall()
    return answer

@connection.connection_handler
def add_question(cursor,new_question,file_path):
    cursor.execute("""INSERT INTO  question(title, message) VALUES """,{'title':new_question['title']}, {'message':new_question['message'], 'file_path': file_path})
    new_question = cursor.fetchall()
    return new_question

@connection.connection_handler
def save_question(cursor, title, message):
    cursor.execute("""INSERT INTO question (submission_time, vote_number, title, message) 
    VALUES (%s, 0, %s, %s)""",
                   [datetime.datetime.now(), title, message])

@connection.connection_handler
def save_answer(cursor, id, message):
    cursor.execute("""INSERT INTO answer (submission_time, vote_number, question_id, message) 
    VALUES (%s, 0, %s, %s)""",
                   [datetime.datetime.now(), id, message])
"""

                   
                   
@app.route('/new-question')
def write_new_question():
    return render_template('new_question.html')


@app.route('/new-question', methods=['POST'])
def post_new_question():
    file = request.files['image']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    new_question = dict(request.form)
    data_handler.add_question(new_question, file.filename)
    return redirect('/')

def question_list():
    table = connection.get_table_from_file(question)
    table.remove(table[0])
    table.reverse()
    return table


def answer_list():
    table = connection.get_table_from_file(answer)
    return table


def save_question(saved_question):
    write = []
    table = connection.get_table_from_file(question)
    write.append(int(table[len(table)-1][0])+1)
    for i in range(3):
        write.append("WOP")
    write.append(saved_question[0])
    write.append(saved_question[1])
    connection.write_table_to_file(question, write)


def save_answer(saved_answer,q_id):
    write = []
    table = connection.get_table_from_file(answer)
    write.append(int(table[len(table)-1][0])+1)
    for i in range(2):
        write.append("WOP")
    write.append(q_id)
    write.append(saved_answer[0])
    connection.write_table_to_file(answer, write)"""
