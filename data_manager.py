import connection
import datetime

@connection.connection_handler
def last_5_questions(cursor):
    cursor.execute("""Select id, title, submission_time, view_number, vote_number, message from question
    order by submission_time desc limit 5""")
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def title_order_by_asc(cursor):
    cursor.execute("""Select id, title, submission_time, message, view_number, vote_number from question
    ORDER BY title ASC """)
    order_by_asc = cursor.fetchall()
    return order_by_asc


@connection.connection_handler
def title_order_by_desc(cursor):
    cursor.execute("""Select id, title, submission_time, message, view_number, vote_number from question
    ORDER BY title DESC """)
    order_by_desc = cursor.fetchall()
    return order_by_desc

@connection.connection_handler
def get_answers(cursor):
    cursor.execute("""Select id, message, submission_time, vote_number, question_id from answer
    order by submission_time desc """)
    answer = cursor.fetchall()
    return answer

'''
@connection.connection_handler
def add_question(cursor, new_question, file_path):
    cursor.execute("""INSERT INTO  question(title, message) VALUES """,
                   {'title': new_question['title']}, {'message': new_question['message'], 'file_path': file_path})
    new_question = cursor.fetchall()
    return new_question
'''
@connection.connection_handler
def save_question(cursor, title, message):
    cursor.execute("""INSERT INTO question (submission_time, view_number, vote_number, title, message) 
    VALUES (%s, 0, 0, %s, %s)""",
                   [datetime.datetime.now(), title, message])

@connection.connection_handler
def save_answer(cursor, id, message):
    cursor.execute("""INSERT INTO answer (submission_time, vote_number, question_id, message) 
    VALUES (%s, 0, %s, %s)""",
                   [datetime.datetime.now(), id, message])


@connection.connection_handler
def view_num(cursor, id):
    cursor.execute("""UPDATE question SET view_number = view_number + 1
     WHERE question.id =%s""",
                   [id])


@connection.connection_handler
def question_up_vote(cursor, id):
    cursor.execute("""UPDATE question SET vote_number = vote_number + 1
     WHERE question.id =%s""",
                   [id])


@connection.connection_handler
def answer_up_vote(cursor, id):
    cursor.execute("""UPDATE answer SET vote_number = vote_number + 1
     WHERE answer.id =%s""",
                   [id])


