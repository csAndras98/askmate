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
    cursor.execute("""Select id, submission_time, vote_number, question_id, message from answer
    order by submission_time desc""")
    answers = cursor.fetchall()
    return answers


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


"""def question_list():
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
