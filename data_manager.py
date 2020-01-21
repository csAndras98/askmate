import connection

@connection.connection_handler
def get_all_questions(cursor):
    cursor.execute("""Select title from question""")
    questions = cursor.fetchall()
    return questions


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
