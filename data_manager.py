import connection
import datetime


@connection.connection_handler
def last_5_questions(cursor):
    cursor.execute("""Select id, title, submission_time, view_number, vote_number, message, uploader from question
    order by submission_time desc limit 5""")
    questions = cursor.fetchall()
    return questions


@connection.connection_handler
def title_order_by_asc(cursor):
    cursor.execute("""Select id, title, submission_time, message, view_number, vote_number, uploader from question
    ORDER BY title ASC """)
    order_by_asc = cursor.fetchall()
    return order_by_asc


@connection.connection_handler
def title_order_by_desc(cursor):
    cursor.execute("""Select id, title, submission_time, message, view_number, vote_number, uploader from question
    ORDER BY title DESC """)
    order_by_desc = cursor.fetchall()
    return order_by_desc


@connection.connection_handler
def get_answers(cursor):
    cursor.execute("""Select id, message, submission_time, vote_number, question_id, uploader from answer
    order by submission_time desc """)
    answer = cursor.fetchall()
    return answer


@connection.connection_handler
def save_question(cursor, title, message, uploader):
    cursor.execute("""INSERT INTO question (submission_time, view_number, vote_number, title, message, uploader) 
    VALUES (%(time)s, 0, 0, %(title)s, %(mess)s, %(user)s)""",
                   {'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), 'title': title, 'mess': message, 'user': uploader})


@connection.connection_handler
def save_answer(cursor, id, message, uploader):
    cursor.execute("""INSERT INTO answer (submission_time, vote_number, question_id, message, uploader) 
    VALUES (%(time)s, 0, %(id)s, %(mess)s, %(user)s)""",
                   {'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), 'id': id, 'mess': message, 'user': uploader})


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


@connection.connection_handler
def check_user_name(cursor, username):
    cursor.execute("""
                    SELECT * FROM users
                    WHERE username = %(username)s
                    """, {'username': username})
    check = cursor.fetchall()
    return check


@connection.connection_handler
def register_user(cursor, user, password):
    cursor.execute("""INSERT INTO users (data, username, hashed_password) 
    VALUES (%(time)s, %(user)s, %(pass)s)""",
                   {'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), 'user': user, 'pass': password})


@connection.connection_handler
def all_user_data(cursor):
    cursor.execute("""
                    SELECT username, data FROM users
                    """)
    all_users = cursor.fetchall()
    return all_users


@connection.connection_handler
def get_user_data(cursor, username):
    cursor.execute("""
                    SELECT username, hashed_password
                    FROM users
                    WHERE username = %(username)s
                    """,
                   {'username': username})
    user_data = cursor.fetchall()
    return user_data
